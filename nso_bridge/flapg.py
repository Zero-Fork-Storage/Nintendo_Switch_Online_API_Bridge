import requests

from nso_bridge.s2s import S2SApi


class FlapgAPI(S2SApi):
    def __init__(self, id_token: str, timestamp: int, guid: str):
        super().__init__(
            id_token, timestamp
        )
        self.flapg_headers = {
            "x-token": id_token,
            "x-time": str(timestamp),
            "x-guid": guid,
            "x-hash": self.get_hash(),
            "x-ver": "3",
            "x-iid": "nso",
        }

        self.url = "https://flapg.com/ika2/api/login?public"

    def get(self):
        response = requests.get(
            url=self.url, 
            headers=self.flapg_headers
        )
        if response.status_code != 200:
            raise Exception(
                f"Flapg API returned status code {response.status_code}"
            )
        return response.json()['result']