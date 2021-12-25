#!/usr/bin/env bash

LANGS=("de")

for lang in "${LANGS[@]}"; do
  pyside6-lupdate src/ui/*.ui -ts "src/i18n/${lang}.ts"
done

mkdir -p src/res/i18n
for file in src/i18n/*.ts; do
  fname=$(echo "${file%.ts}" | sed 's/^src\/i18n\///')
  pyside6-lrelease "$file" -qm "src/res/i18n/${fname}.qm"
done

# shellcheck disable=SC2044
for file in $(find src/ui -name '*.ui'); do
  pyside6-uic "$file" -o "${file%.ui}.py"
done

pyside6-rcc src/res/resources.qrc -o src/res/__init__.py
