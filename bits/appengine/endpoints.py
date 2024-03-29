"""Endpoints Class file."""

import httplib2
import requests
from apiclient.discovery import build
from google.auth import default
from oauth2client import client


class Endpoints:
    """Endpoints class."""

    class Client:
        """Endpoints Client class."""

        def __init__(  # noqa: PLR0913
            self,
            api_key=None,
            base_url="http://localhost:8080",
            api="api",
            version="v1",
            verbose=False,
        ):
            """Initialize a class instance."""
            self.api = api
            self.api_key = api_key
            self.base_url = base_url
            self.verbose = verbose
            self.version = version

            self.api_url = f"{self.base_url}/_ah/api/{self.api}/{self.version}"

            # generate discovery url
            self.discovery_url = f"{self.base_url}/_ah/api/discovery/v1/apis/{self.api}/{self.version}/rest"

            # create credentials from the id_token
            self.http = self.create_http()

            # create a service connection
            self.service = build(
                self.api,
                self.version,
                developerKey=self.api_key,
                discoveryServiceUrl=self.discovery_url,
                http=self.http,
            )

        def create_credentials(self):
            """Create credentials for talking to an endpoints API."""
            id_token = self.generate_id_token()
            return client.AccessTokenCredentials(id_token, "my-user-agent/1.0")

        def create_http(self):
            """Create a httplib2.Http() instance signed witht he credentials."""
            self.credentials = self.create_credentials()
            http = httplib2.Http()
            return self.credentials.authorize(http)

        def generate_id_token(self):
            """Return an ID token that can be used to create credentials."""
            credentials, project = default()
            iam = build("iamcredentials", "v1", credentials=credentials)

            # create audience
            audience = f"{self.base_url}/web-client-id"

            # create service account name
            email = credentials.service_account_email
            if not email or email == "default":
                email = f"{project}@appspot.gserviceaccount.com"
            name = f"projects/-/serviceAccounts/{email}"

            # create body for request
            body = {
                "audience": audience,
                "delegates": [],
                "includeEmail": True,
            }

            # return token
            return (
                iam.projects()
                .serviceAccounts()
                .generateIdToken(
                    name=name,
                    body=body,
                )
                .execute()
                .get("token")
            )

        #
        # Basic Methods (GET, POST, etc.)
        #
        def delete(self, path, credentials=None):
            """Return the response from a DELETE request."""
            url = f"{self.api_url}/{path}"

            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }

            if credentials:
                credentials.apply(headers)

            params = {"key": self.api_key}

            response = requests.delete(
                url,
                headers=headers,
                params=params,
                verify=False,
            )
            response.raise_for_status()
            return response.json()

        def get(self, path, credentials=None, limit=None, pageToken=None):  # noqa: N803
            """Return the response from a GET request."""
            url = f"{self.api_url}/{path}"

            headers = {
                "Accept": "application/json",
            }

            if credentials:
                credentials.apply(headers)

            params = {"key": self.api_key}

            if limit:
                params["limit"] = limit
            if pageToken:
                params["pageToken"] = pageToken  # noqa: N806

            # print(json.dumps(headers, indent=2, sort_keys=True)

            response = requests.get(url, params=params, headers=headers, verify=False)
            response.raise_for_status()
            return response.json()

        def post(self, path, data, credentials=None):
            """Return the response from a POST request."""
            url = f"{self.api_url}/{path}"

            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }

            if credentials:
                credentials.apply(headers)

            params = {"key": self.api_key}

            response = requests.post(
                url,
                headers=headers,
                params=params,
                json=data,
                verify=False,
            )
            response.raise_for_status()
            return response.json()

        def put(self, path, data, credentials=None):
            """Return the response from a PUT request."""
            url = f"{self.api_url}/{path}"

            headers = {
                "Accept": "application/json",
                "Content-Type": "application/json",
            }

            if credentials:
                credentials.apply(headers)

            params = {"key": self.api_key}

            response = requests.put(
                url,
                headers=headers,
                params=params,
                json=data,
                verify=False,
            )

            response.raise_for_status()
            return response.json()

        def get_list(self, path, limit=None, credentials=None):
            """Return a list of all items from a request."""
            response = self.get(path, limit=limit, credentials=credentials)
            if not response:
                return []
            items = response.get("items", [])
            page_token = response.get("nextPageToken")
            while page_token:
                response = self.get(
                    path, limit=limit, pageToken=page_token, credentials=credentials
                )
                items += response.get("items", [])
                page_token = response.get("nextPageToken")
            return items

        def get_paged_list(self, request, params={}):
            """Return a list of all items from a request."""
            response = request.list(**params).execute()
            if not response:
                return []
            items = response.get("items", [])
            page_token = response.get("nextPageToken")
            while page_token:
                params["pageToken"] = page_token
                response = request.list(**params).execute()
                items += response.get("items", [])
                page_token = response.get("nextPageToken")
            return items

        def get_dict(self, path, credentials=None, limit=None, key="id"):
            """Return a dict of items from a resquest."""
            items = self.get_list(path, limit, credentials)
            data = {}
            for i in items:
                k = i.get(key)
                data[k] = i
            return data

        def to_dict(self, items, key="id"):
            """Return a dict of items."""
            data = {}
            duplicates = []
            for i in items:
                k = i.get(key)
                if k not in data:
                    data[k] = i
                else:
                    duplicates.append(i)
            return data, duplicates
