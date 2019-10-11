# -*- coding: utf-8 -*-
"""App Engine Config class file."""

# from flask import request
# from google.cloud import datastore
# from google.cloud import firestore


class Config(object):
    """Config class."""

    def __init__(self, appengine=None, database='firestore', collection='settings'):
        """Initialize a class instance."""
        self.appengine = appengine
        self.database = database
        self.collection = collection

    def config(self, name=None):
        """Return the configuration from Firestore."""
        client = firestore.Client()
        config = {}
        for doc in client.collection(self.collection).stream():
            config[doc.id] = doc.to_dict()
        if name:
            return config.get(name, {})
        return config
