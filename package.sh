#!/bin/sh

PACKAGE="bits_example"

sudo rm -rf build/ dist/ ${PACKAGE}.egg-info/

python3 -m pip install --user --upgrade setuptools wheel

python3 setup.py sdist bdist_wheel

python3 -m pip install --user --upgrade twine

python3 -m twine upload  dist/*
