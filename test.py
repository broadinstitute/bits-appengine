#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test script which demos module functionality."""

import os
import sys

# add bitsapiclient to the path
mypath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(mypath, "bits"))

from bits.appengine import AppEngine  # noqa


def main():
    """Execute the main function."""
    e = AppEngine()
    print(e)


if __name__ == '__main__':
    main()
