#Init
"""
Custom fetch function
"""
from xbox.webapi.api.provider.baseprovider import BaseProvider


class FetchProvider(BaseProvider):
    ACHIEVEMENTS_URL = "https://achievements.xboxlive.com"
    HEADERS_GAME_360_PROGRESS = {'x-xbl-contract-version': '1'}
    HEADERS_GAME_PROGRESS = {'x-xbl-contract-version': '2'}

    def endpoint(self, url):
        """
        Fetch custom Xbox API endpoint

        Args:
            url (str): Url of the endpoint

        Returns:
            :class:`requests.Response`: HTTP Response
        """
        return self.client.session.get(url, headers=self.HEADERS_GAME_PROGRESS)
