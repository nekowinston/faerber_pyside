# IGNQt

[![Build](https://github.com/nekowinston/IGNQt/actions/workflows/main.yml/badge.svg)](https://github.com/nekowinston/IGNQt/actions/workflows/main.yml)
[![CodeQL](https://github.com/nekowinston/IGNQt/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/nekowinston/IGNQt/actions/workflows/codeql-analysis.yml)
[![License](https://img.shields.io/github/license/nekowinston/IGNQt)](https://github.com/nekowinston/IGNQt/blob/master/LICENSE)

A Qt6 GUI for [ImageGoNord](https://github.com/Schrodinger-Hat/ImageGoNord) with
cross-platform support for Linux, macOS, and Windows!

ImageGoNord is a tool which converts your RGB images to different Code Editor
palettes. It defaults to [Nord](https://github.com/arcticicestudio/nord), but
this GUI attempts to make it easy to add support for other colorschemes as well.

## Downloading the binary

While in development, you can download the artifact for your platform from the
[latest build](https://github.com/nekowinston/IGNQt/actions/workflows/main.yml).

## Building locally

I took great care to ensure that building for yourself is as smooth possible.
This project uses [Poetry](https://python-poetry.org/) for dependency 
management. Once all Python dependencies have been installed, and the virtualenv
is activated, building it should be as simple as running:

```shell
python ./make.py
```

This will compile update files for Linguist (i18n), compile `.ui` files to 
Python code, create resource files for Qt, and package with 
[PyInstaller](https://www.pyinstaller.org/) for your system platform.
