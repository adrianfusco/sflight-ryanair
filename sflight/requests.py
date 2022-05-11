import requests


class Request():

    def __init__(
        self: object,
        url: str,
        headers: dict = {
            'Content-type': 'application/json',
            'Accept': 'text/plain'
        },
        payload: dict = {}
    ) -> None:
        self.headers = headers
        self.url = url
        self.payload = payload

    def get_data_from_url(self: object):
        data = requests.get(
                self.url,
                headers=self.headers,
                params=self.payload
        )
        try:
            data.raise_for_status()
        except requests.exceptions.HTTPError as e:
            raise e
        return data.json()
