#!/bin/env bash

LANGS=("de")

for lang in "${LANGS[@]}"; do
  pyside6-lupdate src/ui/*.ui -ts src/i18n/$lang.ts
done

find src/i18n -name "*.ts" -exec bash -c '
  fname="${1%.ts}"
  pyside6-lrelease "$1" -qm "${fname/src\/i18n\//src\/res\/i18n\/}.qm"
' bash {} \;

find src/ui -name "*.ui" -exec bash -c '
  pyside6-uic "$1" -o "${1%.ui}.py"
' bash {} \;

pyside6-rcc src/res/resources.qrc -o src/res/__init__.py
