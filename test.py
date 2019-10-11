#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test script which demos module functionality."""

import os
import sys

# add bitsapiclient to the path
mypath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(mypath, "bits"))

from bits.appengine import AppEngine  # noqa
from bits.appengine.endpoints import Endpoints

# debug_user = {
#     'email': 'karlsson@broadinstitue.org',
#     'id': '111375498507364395026',
# }


def main():
    """Execute the main function."""
    # appengine = AppEngine()
    client = Endpoints.Client(
        api='bitsdb',
        base_url='https://broad-bitsdb-api.appspot.com',
        # debug=True
    )
    request = client.service.people().list()
    people = request.execute()
    print('People: {}'.format(len(people)))


if __name__ == '__main__':
    main()
