import requests

from .constants import BASE_URL, DEFAULT_HEADERS
from .exceptions import RequestError

from  community import CommunityAPI
from  blogs import BlogsAPI


class KarboAI:
    def __init__(self, timeout=30):
        self.base_url = BASE_URL
        self.timeout = timeout

        self.session = requests.Session()
        self.session.headers.update(DEFAULT_HEADERS)

        self.community = CommunityAPI(self)
        self.blogs = BlogsAPI(self)

    def get(self, endpoint, params=None):
        url = f"{self.base_url}{endpoint}"

        try:
            response = self.session.get(
                url,
                params=params,
                timeout=self.timeout
            )

            response.raise_for_status()

            return response.json()

        except requests.RequestException as e:
            raise RequestError(str(e))
