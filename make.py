import argparse
import glob
import os
import pathlib
import sys
from os import path
from subprocess import Popen, PIPE

import PyInstaller.__main__ as pyinstaller
import PySide6

parser = argparse.ArgumentParser()
parser.add_argument(
    "--skip-build",
    help="skips PyInstaller. useful in dev.",
    action="store_true",
    default=False,
)
args = parser.parse_args()


# modified qt_tool_wrapper from PySide6.scripts
def qtt(qt_tool, args, libexec=False):
    pyside_dir = pathlib.Path(PySide6.__file__).resolve().parent
    if libexec and sys.platform != "win32":
        exe = pyside_dir / "Qt" / "libexec" / qt_tool
    else:
        exe = pyside_dir / qt_tool
    cmd = [os.fspath(exe)] + args
    proc = Popen(cmd, stdout=PIPE, stderr=PIPE)
    out, err = proc.communicate()

    if err:
        msg = err.decode("utf-8")
        command = " ".join(cmd)
        print(f"Error: {msg}\nwhile executing '{command}'")
        sys.exit(1)

    if out.decode("utf-8") != "":
        print(out.decode("utf-8"))


def run_lupdate(languages):
    print("lupdate:")
    for lang in languages:
        for file in glob.glob("src/**/*.ui", recursive=True):
            dest = "src/i18n/{}.ts".format(lang)
            qtt("lupdate", [file, "-ts", dest])


def run_lrelease():
    print("lrelease:")
    destpath = path.join("src", "res", "i18n")

    if not os.path.isdir(destpath):
        os.mkdir("src/res/i18n")

    for file in glob.glob("src/i18n/*.ts"):
        language = path.splitext(path.basename(file))[0]
        dest = path.join(destpath, "{}.qm".format(language))
        qtt("lrelease", [file, "-qm", dest])


def run_uic():
    for file in glob.glob("src/ui/**/*.ui", recursive=True):
        dest = "{}.py".format(path.splitext(file)[0])
        print("uic: {} -> {}".format(file, dest))
        qtt("uic", ["-g", "python", file, "-o", dest], True)


def run_rcc():
    file = "src/res/resources.qrc"
    dest = "src/res/__init__.py"
    print("rcc: {} -> {}".format(file, dest))
    qtt("rcc", ["-g", "python", file, "-o", dest], True)


if __name__ == "__main__":
    # supported languages for i18n
    languages = ["de"]

    # update files for linguist
    run_lupdate(languages)
    # compile translation files
    run_lrelease()
    # compile designer files to python code
    run_uic()
    # finally, make python resource file
    run_rcc()

    if not args.skip_build:
        pyinstaller.run([".pyinstaller/build.spec"])

    # additional CI cleanup operations
    if os.environ.get("CI"):
        if sys.platform == "darwin":
            os.remove("dist/IGNQt")
