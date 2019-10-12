# -*- coding: utf-8 -*-
# Copyright 2018 Broad Institute of MIT and Harvard
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from setuptools import setup, find_packages


setup(
    name='bits-appengine',

    version='1.0.6',

    description='BITS App Engine',
    long_description='',

    author='Lukas Karlsson',
    author_email='karlsson@broadinstitute.org',

    license='Apache Software License',

    packages=find_packages(),
    install_requires=[
        'flask==1.0.2',
        'google-cloud-datastore',
        'google-cloud-firestore',
        'google-api-python-client',
        'httplib2',
        'oauth2client',
    ],

    zip_safe=False,
)
