#Init
"""
Custom fetch function
"""
from xbox.webapi.api.provider.baseprovider import BaseProvider


class FetchProvider(BaseProvider):
    def endpoint(self, url, xbl_headers):
        """
        Fetch custom Xbox API endpoint

        Args:
            url (str): Url of the endpoint

        Returns:
            :class:`requests.Response`: HTTP Response
        """
        return self.client.session.get(url, headers=xbl_headers)
