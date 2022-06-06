import time
import uuid
import requests

from app.flapg import FlapgAPI


class NintendoSwitchOnlineLogin:
    def __init__(self, nso_app_version: str, user_info: dict, user_lang: str, access_token, guid):
        self.headers = {
            'Host': 'api-lp1.znc.srv.nintendo.net',
            'Accept-Language': user_lang,
            'User-Agent': 'com.nintendo.znca/' + nso_app_version + ' (Android/12.1.2)',
            'Accept': 'application/json',
            'X-ProductVersion': nso_app_version,
            'Content-Type': 'application/json; charset=utf-8',
            'Connection': 'Keep-Alive',
            'Authorization': 'Bearer',
            'X-Platform': 'Android',
            'Accept-Encoding': 'gzip'
        }
        self.url = 'https://api-lp1.znc.srv.nintendo.net/v3/Account/Login'
        self.timestamp = int(time.time())
        self.guid = guid
        self.user_info = user_info
        self.access_token = access_token
        self.flapg = FlapgAPI(self.access_token, self.timestamp, self.guid).get()
        self.account = None

        self.body = {
            'parameter': {
                'f': self.flapg['f'],
                'naIdToken': self.flapg['p1'],
                'timestamp': self.flapg['p2'],
                'requestId': self.flapg['p3'],
                'naCountry': self.user_info['country'],
                'naBirthday': self.user_info['birthday'],
                'language': self.user_info['language'],
            },
        }

    def to_account(self):
        response = requests.post(
            url=self.url, headers=self.headers, json=self.body
        )
        if response.status_code != 200:
            raise Exception(
                f"Error: {response.status_code}"
            )
        self.account = response.json()
        return self.account


class NintendoSwitchOnlineAPI:
    def __init__(self, nso_app_version: str, user_info: dict, service_token: str, user_lang: str = "en-US"):
        self.nso_app_version = nso_app_version
        self.url = 'https://api-lp1.znc.srv.nintendo.net'
        self.headers = {
            'X-ProductVersion': nso_app_version,
            'X-Platform': 'iOS',
            'User-Agent': 'Coral/2.0.0 (com.nintendo.znca; build:1489; iOS 15.3.1) Alamofire/5.4.4',
            'Accept': 'application/json',
            'Content-Type': 'application/json; charset=utf-8',
            'Host': 'api-lp1.znc.srv.nintendo.net',
            'Connection': 'Keep-Alive',
            'Accept-Encoding': 'gzip',
        }

        self.user_lang = user_lang
        self.user_info = user_info
        self.token = service_token
        self.id_token = self.token['id_token']
        self.access_token = self.token['access_token']
        self.guid = str(uuid.uuid4())

        self.login = {
            'login': None,
            'time': 0
        }

    def sync_login(self):
        login = NintendoSwitchOnlineLogin(
            self.nso_app_version,
            self.user_info,
            self.user_lang,
            self.access_token,
            self.guid
        )
        login.to_account()

        self.headers['Authorization'] = f"Bearer {login.account['result']['webApiServerCredential']['accessToken']}"
        self.login = {
            'login': login,
            'time': time.time(),
        }