# -*- coding: utf-8 -*-
"""Example class file."""

from flask import request
from google.cloud import firestore


from bits.appengine.config import Config
from bits.appengine.user import User


class AppEngine(object):
    """AppEngine class."""

    def __init__(
        self,
        database='firestore',
        project=None,
        user_collection='users',
        debug_user=None
    ):
        """Initialize an Example class instance."""
        self.database = database
        self.debug_user = debug_user

    def config(self):
        """Return a Config instance."""
        return Config(
            appengine=self,
            database=self.database,
        )

    def user(self):
        """Return a User instance."""
        return User(
            appengine=self,
            database=self.database,
        )
