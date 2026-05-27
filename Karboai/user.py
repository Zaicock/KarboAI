import requests

class UserAPI:
    def __init__(self, base_url, headers):
        self.base_url = base_url
        self.headers = headers

    def get(self, user_id: str, community_id: str):
        """Get user info by ID"""
        url = f"{self.base_url}/user/{user_id}"

        params = {
            "community_id": community_id
        }

        res = requests.get(url, params=params, headers=self.headers)
        return res.json() if res.headers.get("content-type","").startswith("application/json") else res.text

    def resolve(self, username: str):
        """Convert username -> user info / id"""
        url = f"{self.base_url}/links/resolve-public"

        params = {
            "link": f"/user/{username}"
        }

        res = requests.get(url, params=params, headers=self.headers)
        return res.json() if res.headers.get("content-type","").startswith("application/json") else res.text
