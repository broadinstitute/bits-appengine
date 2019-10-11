#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test script which demos module functionality."""

import os
import sys

# add bitsapiclient to the path
mypath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(mypath, "bits"))

from bits.appengine import AppEngine  # noqa

debug_user = {
    'email': 'karlsson@broadinstitue.org',
    'id': '111375498507364395026',
}


def main():
    """Execute the main function."""
    ae = AppEngine(debug_user=debug_user)
    user = ae.user()
    print(user)


if __name__ == '__main__':
    main()
