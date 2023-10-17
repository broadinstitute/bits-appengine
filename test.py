#!/usr/bin/env python
"""Test script which demos module functionality."""

import os
import sys

# from bits.auth import Auth
# from bits.settings import Settings

# add bitsapiclient to the path
mypath = os.path.dirname(os.path.realpath(__file__))
sys.path.append(os.path.join(mypath, "bits"))
# sys.path.append(os.path.join(mypath, "bits-api-python-client"))

from bits.appengine import AppEngine  # noqa
from bits.appengine.endpoints import Endpoints  # noqa

# debug_user = {
#     'email': 'karlsson@broadinstitue.org',
#     'id': '111375498507364395026',
# }

# settings = Settings().get()
# auth = Auth(settings)


def main():
    """Execute the main function."""
    # appengine = AppEngine()
    # users = appengine.user().get_stored_users()
    # print('Users: {}'.format(len(users)))
    # return

    client = Endpoints.Client(
        api="bitsdb",
        api_key="****",
        base_url="https://broad-bitsdb-api.appspot.com",
        version="v1",
        verbose=True,
    )
    # client = auth.bitsdbapi()
    people = client.service.people().list(limit=1000).execute().get("items", [])
    # people = request.execute().get('items', [])
    print(f"People: {len(people)}")
    # print(people)
    # print(client.service.buildings().list().execute().get('items', []))


if __name__ == "__main__":
    main()
