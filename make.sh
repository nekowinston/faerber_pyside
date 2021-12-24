#!/bin/env bash

# use hash seed for reproducibility
export PYTHONHASHSEED=2147483647

pyinstaller .pyinstaller/build.spec

# let Python be unpredictable again (default)
unset PYTHONHASHSEED
