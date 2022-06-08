import requests


class S2SApi:
    def __init__(self, naIdToken: str, timestamp: int, version: str = "unknown"):
        self.version = version
        self.naIdToken = naIdToken
        self.timestamp = timestamp

        self.headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
            'User-Agent': 'NintendoSwitchOnlineAPIBridge/%s' % self.version,
        }
        self.body = {
            "naIdToken": self.naIdToken,
            "timestamp": self.timestamp,
        }

        self.s2s_api_url = "https://elifessler.com/s2s/api/gen2"

    def get_hash(self):
        response = requests.post(
            url=self.s2s_api_url,
            headers=self.headers,
            data=self.body
        )
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code}")
        return response.json()["hash"]
        