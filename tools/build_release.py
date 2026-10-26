# SPDX-License-Identifier: GPL-3.0-or-later
# Copyright (C) 2026 Nexxus Drako Multimedia
"""Build an LMASTER Mod release: one xdelta patch per edition, checked,
hashed and zipped with the player docs.

For each edition in release.toml it runs LMAST-Reverse's patch_disc.py on
the vanilla Redump image, makes a VCDIFF (xdelta3-format) patch with
vcdiff.py, applies that patch again to a scratch image and checks the
result matches the built disc byte for byte (by SHA-1), then records the
patched disc's hashes. If xdelta3 is on PATH, the patch is also applied
with it, so a release is known to work in the patchers players use.

It also writes LMAST-Reverse's widescreen patch for each edition under the
edition's own PCSX2 CRC, after checking that none of the patch's writes is
at or next to a byte the edition changed in SLES_541.51.

Usage (from this repo's root):
    python tools/build_release.py <vanilla.iso> [--keep-isos] [--allow-dirty]

Writes build/ (scratch, git-ignored) and dist/ (git-ignored):
    dist/LMASTER-Mod-<version>/            the folder players get
        LMASTER-Mod-<version>-Full.xdelta
        LMASTER-Mod-<version>-Lite.xdelta
        widescreen/SLES-54151_<CRC>.pnach   one per edition
        README.md  CHANGELOG.md  LICENSE
        HASHES.txt   the disc players need, and what each patch makes
        SHA256SUMS   sha256sum -c format, for the files in the folder
    dist/LMASTER-Mod-<version>.zip         that folder, zipped
    dist/LMASTER-Mod-<version>.zip.sha256
Standard library only; Python 3.11+ (tomllib).
"""
import hashlib
import os
import re
import shutil
import struct
import subprocess
import sys
import time
import tomllib
import zipfile
import zlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT = "LMASTER-Mod"
TEST_SWITCHES = ("skip-tutorial", "launcher")
# semver.org's own regular expression, without the build-metadata group's names.
SEMVER = re.compile(r"^(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)"
                    r"(?:-((?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*)"
                    r"(?:\.(?:0|[1-9]\d*|\d*[a-zA-Z-][0-9a-zA-Z-]*))*))?"
                    r"(?:\+([0-9a-zA-Z-]+(?:\.[0-9a-zA-Z-]+)*))?$")
PLAYER_DOCS = ("README.md", "CHANGELOG.md", "LICENSE")
VANILLA_CRC = "3CB245D5"
WIDESCREEN = os.path.join("PNACH", "SLES-54151_%s.pnach" % VANILLA_CRC)
PNACH_WRITE = re.compile(r"^patch=\d+,EE,([0-9a-fA-F]+),(byte|short|word|double|bytes),([0-9a-fA-F]+)")
PNACH_SIZES = {"byte": 1, "short": 2, "word": 4, "double": 8}


def fail(msg):
    raise SystemExit("error: " + msg)


def hashes(path, label=None):
    """Size, CRC-32, MD5, SHA-1 and SHA-256 of a file, in one pass."""
    crc, md5, sha1, sha256 = 0, hashlib.md5(), hashlib.sha1(), hashlib.sha256()
    size, done_at = os.path.getsize(path), time.time()
    with open(path, "rb") as f:
        while chunk := f.read(1 << 24):
            crc = zlib.crc32(chunk, crc)
            md5.update(chunk)
            sha1.update(chunk)
            sha256.update(chunk)
    if label and size > 1 << 28:
        print("  hashed %s in %.0f s" % (label, time.time() - done_at))
    return {"size": size, "crc32": "%08x" % crc, "md5": md5.hexdigest(),
            "sha1": sha1.hexdigest(), "sha256": sha256.hexdigest()}


def run(cmd, cwd, log):
    """Run a command, echo it and its output, and keep both in the build log."""
    print("$ " + " ".join(cmd))
    log.write("$ %s\n" % " ".join(cmd))
    p = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True, errors="replace")
    out = p.stdout + p.stderr
    log.write(out + "\n")
    log.flush()
    if p.returncode:
        print(out)
        fail("%s exited with %d (see build/build.log)" % (cmd[1], p.returncode))
    return out


def git(repo, *args):
    return subprocess.run(["git", "-C", repo, *args], capture_output=True, text=True,
                          check=True).stdout.strip()


def load_config():
    with open(os.path.join(ROOT, "release.toml"), "rb") as f:
        cfg = tomllib.load(f)
    with open(os.path.join(ROOT, "VERSION")) as f:
        version = f.read().strip()
    if not SEMVER.match(version):
        fail("VERSION %r is not a semantic version (semver.org)" % version)
    for ed in cfg["edition"]:
        bad = set(ed["mod"].split(",")) & set(TEST_SWITCHES)
        if bad:
            fail("edition %s includes test-only switch %s" % (ed["name"], ", ".join(bad)))
    return cfg, version


def check_changelog(version):
    with open(os.path.join(ROOT, "CHANGELOG.md"), encoding="utf-8") as f:
        if "## [%s]" % version not in f.read():
            fail("CHANGELOG.md has no '## [%s]' section; add one before releasing" % version)


def check_source(cfg, allow_dirty):
    repo = os.path.normpath(os.path.join(ROOT, cfg["source"]["lmast_reverse"]))
    if not os.path.isfile(os.path.join(repo, "SRC", "patch_disc.py")):
        fail("no LMAST-Reverse checkout at %s (release.toml [source])" % repo)
    head = git(repo, "rev-parse", "HEAD")
    if head != cfg["source"]["commit"]:
        fail("LMAST-Reverse is at %s, release.toml pins %s" % (head[:12], cfg["source"]["commit"][:12]))
    if git(repo, "status", "--porcelain", "--untracked-files=no") and not allow_dirty:
        fail("LMAST-Reverse has uncommitted changes; commit them or pass --allow-dirty")
    return repo, head


def check_vanilla(path, cfg):
    print("Checking the vanilla disc %s" % path)
    want = cfg["vanilla"]
    got = hashes(path, "the vanilla disc")
    for key in ("size", "crc32", "md5", "sha1"):
        if got[key] != want[key]:
            fail("vanilla disc %s is %s, Redump's is %s: not the Redump dump (%s)"
                 % (key, got[key], want[key], want["redump"]))
    return got


def xdelta3_check(vanilla, patch, want_sha1, scratch, log):
    exe = shutil.which("xdelta3")
    if not exe:
        print("  xdelta3 not on PATH: skipping the cross-check")
        return "not run (xdelta3 not installed)"
    run([exe, "-d", "-f", "-s", vanilla, patch, scratch], ROOT, log)
    sha1 = hashes(scratch)["sha1"]
    os.remove(scratch)
    if sha1 != want_sha1:
        fail("xdelta3 made %s from %s, expected %s" % (sha1, patch, want_sha1))
    return "passed"


def executable(iso, repo):
    """SLES_541.51 from a disc image, read with LMAST-Reverse's ISO9660 walker."""
    sys.path.insert(0, os.path.join(repo, "SRC"))
    from extract_disc import walk_iso
    with open(iso, "rb") as f:
        e = next(e for e in walk_iso(f) if e.path.upper().startswith("SLES_541.51"))
        f.seek(e.extent * 2048)
        return f.read(e.size)


def changed_addresses(old, new):
    """EE memory addresses of the bytes that differ between two copies of the
    executable, through its PT_LOAD program headers."""
    if len(old) != len(new):
        fail("the edition's SLES_541.51 changed size; check the widescreen patch by hand")
    phoff, = struct.unpack_from("<I", old, 0x1c)
    phnum, = struct.unpack_from("<H", old, 0x2c)
    loads = []
    for i in range(phnum):
        kind, off, vaddr, _, filesz = struct.unpack_from("<5I", old, phoff + 32 * i)
        if kind == 1:
            loads.append((off, vaddr, filesz))
    return {vaddr + i - off for i in range(len(old)) if old[i] != new[i]
            for off, vaddr, filesz in loads if off <= i < off + filesz}


def pnach_writes(text):
    """(start, end) of every EE write in a .pnach."""
    out = []
    for line in text.splitlines():
        m = PNACH_WRITE.match(line.strip())
        if m:
            start = int(m[1], 16)
            size = len(m[3]) // 2 if m[2] == "bytes" else PNACH_SIZES[m[2]]
            out.append((start, start + size))
    return out


def write_widescreen(vanilla_exe, iso, crc, repo, out_dir):
    """The widescreen patch under the edition's CRC, if none of its writes is
    at or within 64 bytes of a byte the edition changed; returns the line
    HASHES.txt gives it."""
    with open(os.path.join(repo, WIDESCREEN), encoding="utf-8") as f:
        text = f.read()
    changed = changed_addresses(vanilla_exe, executable(iso, repo))
    writes = pnach_writes(text)
    clash = sorted(a for a in changed for lo, hi in writes if lo - 64 <= a < hi + 64)
    if clash:
        fail("the widescreen patch writes at or next to %d byte(s) the edition changed (first 0x%x)"
             % (len(clash), clash[0]))
    text = text.replace("(%s)" % VANILLA_CRC, "(%s, LMASTER Mod)" % crc, 1)
    folder = os.path.join(out_dir, "widescreen")
    os.makedirs(folder, exist_ok=True)
    name = "SLES-54151_%s.pnach" % crc
    with open(os.path.join(folder, name), "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    return "widescreen/%s (its %d writes miss all %d changed program bytes)" % (
        name, len(writes), len(changed))


def build_edition(ed, version, vanilla, vanilla_exe, repo, build, out_dir, keep, log):
    tag = "%s-%s-%s" % (PROJECT, version, ed["name"])
    iso = os.path.join(build, tag + ".iso")
    patch = os.path.join(out_dir, tag + ".xdelta")
    check = os.path.join(build, tag + ".check.iso")
    args = ed.get("args", [])
    print("\n== %s (--mod %s) ==" % (ed["name"], " ".join([ed["mod"]] + args)))
    py = sys.executable
    out = run([py, "SRC/patch_disc.py", "patch", vanilla, iso, "--mod", ed["mod"]] + args,
              repo, log)
    crc = re.search(r"PCSX2 CRC of the executable ([0-9A-F]{8})", out)
    built = hashes(iso, tag + ".iso")
    run([py, "SRC/vcdiff.py", "make", vanilla, iso, patch], repo, log)
    out = run([py, "SRC/vcdiff.py", "apply", vanilla, patch, check], repo, log)
    if built["sha1"] not in out:
        fail("re-applying %s didn't reproduce the built disc" % patch)
    os.remove(check)
    print("  patch re-applied: result matches the built disc")
    x3 = xdelta3_check(vanilla, patch, built["sha1"], check, log)
    pcsx2_crc = crc.group(1) if crc else VANILLA_CRC
    ws = write_widescreen(vanilla_exe, iso, pcsx2_crc, repo, out_dir)
    print("  " + ws)
    if not keep:
        os.remove(iso)
    return {"edition": ed, "patch": patch, "result": built, "xdelta3": x3,
            "pcsx2_crc": pcsx2_crc, "widescreen": ws}


def write_hashes(path, version, vanilla, results, head, cfg):
    v = cfg["vanilla"]
    lines = ["LMASTER Mod %s" % version, "",
             "Built from LMAST-Reverse commit %s" % head,
             "(%s/commit/%s)" % (cfg["source"]["upstream"], head), "",
             "THE DISC YOU NEED (before patching)",
             "  %s" % v["name"], "  Redump: %s" % v["redump"]]
    lines += ["  %-8s %s" % (k, vanilla[k] if k != "size" else "{:,} bytes".format(vanilla[k]))
              for k in ("size", "crc32", "md5", "sha1")]
    for r in results:
        res = r["result"]
        lines += ["", "%s EDITION: what %s makes" % (r["edition"]["name"].upper(),
                                                     os.path.basename(r["patch"]))]
        lines += ["  %-8s %s" % (k, res[k] if k != "size" else "{:,} bytes".format(res[k]))
                  for k in ("size", "crc32", "md5", "sha1")]
        lines.append("  PCSX2 CRC %s" % r["pcsx2_crc"])
        lines.append("  widescreen %s" % r["widescreen"])
        lines.append("  checked: re-applied and matched; xdelta3 %s" % r["xdelta3"])
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(lines) + "\n")


def release_files(folder):
    """Every file under the release folder, as "/"-separated relative paths."""
    out = []
    for top, _, files in os.walk(folder):
        out += [os.path.relpath(os.path.join(top, n), folder).replace(os.sep, "/") for n in files]
    return sorted(out)


def write_sha256sums(folder):
    names = [n for n in release_files(folder) if n != "SHA256SUMS"]
    with open(os.path.join(folder, "SHA256SUMS"), "w", newline="\n") as f:
        for n in names:
            f.write("%s  %s\n" % (hashes(os.path.join(folder, n))["sha256"], n))


def zip_folder(folder):
    zpath = folder + ".zip"
    base = os.path.basename(folder)
    with zipfile.ZipFile(zpath, "w", zipfile.ZIP_DEFLATED, compresslevel=9) as z:
        for n in release_files(folder):
            z.write(os.path.join(folder, n), "%s/%s" % (base, n))
    with open(zpath + ".sha256", "w", newline="\n") as f:
        f.write("%s  %s\n" % (hashes(zpath)["sha256"], os.path.basename(zpath)))
    return zpath


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    flags = {a for a in argv[1:] if a.startswith("--")}
    if len(args) != 1 or flags - {"--keep-isos", "--allow-dirty"}:
        print(__doc__)
        return 2
    vanilla_path = os.path.abspath(args[0])
    cfg, version = load_config()
    check_changelog(version)
    repo, head = check_source(cfg, "--allow-dirty" in flags)
    vanilla = check_vanilla(vanilla_path, cfg)
    vanilla_exe = executable(vanilla_path, repo)

    build = os.path.join(ROOT, "build")
    out_dir = os.path.join(ROOT, "dist", "%s-%s" % (PROJECT, version))
    os.makedirs(build, exist_ok=True)
    if os.path.isdir(out_dir):
        shutil.rmtree(out_dir)
    os.makedirs(out_dir)

    start = time.time()
    with open(os.path.join(build, "build.log"), "w", encoding="utf-8") as log:
        log.write("LMASTER Mod %s from LMAST-Reverse %s\n\n" % (version, head))
        results = [build_edition(ed, version, vanilla_path, vanilla_exe, repo, build, out_dir,
                                 "--keep-isos" in flags, log) for ed in cfg["edition"]]
    for name in PLAYER_DOCS:
        shutil.copy2(os.path.join(ROOT, name), out_dir)
    write_hashes(os.path.join(out_dir, "HASHES.txt"), version, vanilla, results, head, cfg)
    write_sha256sums(out_dir)
    zpath = zip_folder(out_dir)
    print("\nDone in %.0f min: %s" % ((time.time() - start) / 60, os.path.relpath(zpath, ROOT)))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
