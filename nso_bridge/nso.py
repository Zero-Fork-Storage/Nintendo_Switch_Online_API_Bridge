import base64
import json
import pickle
import time
import uuid

import keyring
import requests

from nso_bridge import __version__
from nso_bridge.metadata import ZNCA_PLATFORM, ZNCA_USER_AGENT, ZNCA_VERSION
from nso_bridge.nsa import NintendoSwitchAccount
from nso_bridge.utils import check_friend_code_hash, is_friend_code


class mAPI:
    def __init__(self, id_token: str, step: int):
        self.id_token = id_token
        self.step = step

        self.api_header = {
            "User-Agent": f"Nintendo_Switch_Online_Bridge/{__version__}",
            "Content-Type": "application/json; charset=utf-8",
        }
        self.api_body = {"token": id_token, "hashMethod": step}
        self.api_url = "https://api.imink.app/f"

    def get_response(self):
        api_resp = requests.post(
            url=self.api_url, data=json.dumps(self.api_body), headers=self.api_header
        )
        if api_resp.status_code != 200:
            raise Exception(f"{api_resp.json()}")
        rs = api_resp.json()
        f = rs["f"]
        uuid = rs["request_id"]
        timestamp = rs["timestamp"]
        return {"f": f, "uuid": uuid, "timestamp": timestamp}


class NintendoSwitchOnlineLogin:
    def __init__(
        self,
        user_info: dict,
        user_lang: str,
        access_token,
        guid,
        id_token,
    ):
        self.headers = {
            "X-Platform": ZNCA_PLATFORM,
            "X-ProductVersion": ZNCA_VERSION,
            "Accept-Language": user_lang,
            "User-Agent": "com.nintendo.znca/" + ZNCA_VERSION + " (Android/12.1.2)",
            "Authorization": "Bearer",
            "Content-Type": "application/json; charset=utf-8",
            "Host": "api-lp1.znc.srv.nintendo.net",
        }
        self.url = "https://api-lp1.znc.srv.nintendo.net/v3/Account/Login"
        self.timestamp = int(time.time())
        self.guid = guid
        self.user_info = user_info
        self.access_token = access_token
        self.id_token = id_token
        self.flapg = self.mFlag()
        self.account = None

        self.body = {
            "parameter": {
                "f": self.flapg["f"],
                "naIdToken": self.id_token,
                "timestamp": self.flapg["timestamp"],
                "requestId": self.flapg["uuid"],
                "naCountry": self.user_info["country"],
                "naBirthday": self.user_info["birthday"],
                "language": self.user_info["language"],
            },
        }

    def mFlag(self):
        return mAPI(self.id_token, 1).get_response()

    def to_account(self):
        response = requests.post(url=self.url, headers=self.headers, json=self.body)
        if response.status_code != 200:
            raise Exception(f"Error: {response.status_code}")
        self.account = response.json()
        return self.account


class NintendoSwitchOnlineAPI:
    def __init__(
        self,
        session_token: str,
        user_lang: str = "en-US",
        nso_app_version: str | None = None,
    ):
        self.nsa = NintendoSwitchAccount()
        self.nso_app_version = ZNCA_VERSION or nso_app_version
        self.url = "https://api-lp1.znc.srv.nintendo.net"
        self.headers = {
            "X-Platform": ZNCA_PLATFORM,
            "X-ProductVersion": ZNCA_VERSION or self.nso_app_version,
            "User-Agent": ZNCA_USER_AGENT,
            "Content-Type": "application/json; charset=utf-8",
            "Host": "api-lp1.znc.srv.nintendo.net",
        }

        self.user_lang = user_lang

        if session_token is None:
            session_token = self.nsa.nso_login(self.nsa.m_input)

        self.token = self.nsa.get_service_token(session_token=session_token)
        self.id_token = self.token.get("id_token")
        self.access_token = self.token.get("access_token")
        self.guid = str(uuid.uuid4())
        self.user_info = self.nsa.get_user_info(self.access_token)
        self.login = {"login": None, "time": 0}
        self.NSOL = NintendoSwitchOnlineLogin(
            self.user_info,
            self.user_lang,
            self.access_token,
            self.guid,
            self.id_token,
        )

    def getAnnouncements(self):
        """Get information of announcements."""
        resp = requests.post(
            url=self.url + "/v1/Announcement/List", headers=self.headers
        )
        if resp.status_code != 200:
            raise Exception(f"Error: {resp.status_code}")
        return resp.json()

    # Web Service API
    def getWebServices(self):
        """Get information of web services registered to Nintendo Switch account."""
        resp = requests.post(
            url=self.url + "/v1/Game/ListWebServices", headers=self.headers
        )
        if resp.status_code != 200:
            raise Exception(f"Error: {resp.status_code}")
        return resp.json()

    # def getGameWebServiceToken(self, game_id: str):
    #   resp = requests.post(
    #        url=self.url + "/v2/Game/GetWebServiceToken",
    #        json={
    #            "parameter": {
    #                "id": game_id,
    #                "registrationToken": "",
    #                "f": self.NSOL.flapg["f"],
    #                "requestId": self.NSOL.flapg["uuid"],
    #                "timestamp": self.NSOL.flapg["timestamp"],
    #            }
    #        },
    #        headers=self.headers
    #    )
    #    if resp.status_code != 200:
    #        raise Exception(f"Error: {resp.status_code}")
    #    return resp.json()

    def getActiveEvent(self):
        """Get information of active events."""
        resp = requests.post(
            url=self.url + "/v1/Event/GetActiveEvent", headers=self.headers
        )
        if resp.status_code != 200:
            raise Exception(f"Error: {resp.status_code}")
        return resp.json()

    def getEvent(self, user_id: int):
        """Get information of events."""
        resp = requests.post(
            url=self.url + "/v1/Event/Show",
            headers=self.headers,
            json={"parameter": {"id": user_id}},
        )
        if resp.status_code != 200:
            raise Exception(f"Error: {resp.status_code}")
        return resp.json()

    def getUser(self, user_id: int):
        """Get information of user."""
        resp = requests.post(
            url=self.url + "/v3/User/Show",
            headers=self.headers,
            json={"parameter": {"id": user_id}},
        )
        if resp.status_code != 200:
            raise Exception(f"Error: {resp.status_code}")
        return resp.json()

    def getCurrentUser(self):
        """Get information of My Nintendo Switch Account."""
        resp = requests.post(url=self.url + "/v3/User/ShowSelf", headers=self.headers)
        if resp.status_code != 200:
            raise Exception(f"Error: {resp.status_code}")
        return resp.json()

    def getCurrentUserPermissions(self):
        """Get information of current user permissions."""
        resp = requests.post(
            url=self.url + "/v3/User/Permissions/ShowSelf", headers=self.headers
        )
        if resp.status_code != 200:
            raise Exception(f"Error: {resp.status_code}")
        return resp.json()

    def getFriends(self):
        """Get information of friends registered to Nintendo Switch account."""
        resp = requests.post(url=self.url + "/v3/Friend/List", headers=self.headers)
        if resp.status_code != 200:
            raise Exception(f"Error: {resp.status_code}")
        return resp.json()

    def getFriendCodeUrl(self):
        """Get information of friend code URL."""
        resp = requests.post(
            url=self.url + "/v3/Friend/CreateFriendCodeUrl", headers=self.headers
        )
        if resp.status_code != 200:
            raise Exception(f"Error: {resp.status_code}")
        return resp.json()

    def getUserByFriendCode(self, friend_code: str, _hash: str | None = None):
        if not is_friend_code(friend_code):
            raise Exception("Invalid friend code")
        if hash is not None:
            if not check_friend_code_hash(_hash):
                raise Exception("Invalid hash")
            else:
                resp_hash = requests.post(
                    url=self.url + "/v3/Friend/GetUserByFriendCodeHash",
                    headers=self.headers,
                    json={
                        "parameter": {
                            "friendCode": friend_code,
                            "friendCodeHash": _hash,
                        }
                    },
                )
                if resp_hash.status_code != 200:
                    raise Exception(f"Error: {resp_hash.status_code}")
        else:
            resp = requests.post(
                url=self.url + "/v3/Friend/GetUserByFriendCode",
                headers=self.headers,
                json={
                    "parameter": {
                        "friendCode": friend_code,
                    }
                },
            )
            if resp.status_code != 200:
                raise Exception(f"Error: {resp.status_code}")
            return resp.json()

    def sendFriendRequest(self, nsa_id: int):
        """Send friend request."""
        resp = requests.post(
            url=self.url + "/v3/FriendRequest/Create",
            headers=self.headers,
            json={"parameter": {"nsaId": nsa_id}},
        )
        if resp.status_code != 200:
            raise Exception(f"Error: {resp.status_code}")
        return resp.json()

    def addFavouriteFriend(self, nsa_id: int):
        """Add favourite friend."""
        resp = requests.post(
            url=self.url + "/v3/Friend/Favorite/Create",
            headers=self.headers,
            json={"parameter": {"nsaId": nsa_id}},
        )
        if resp.status_code != 200:
            raise Exception(f"Error: {resp.status_code}")
        return resp.json()

    def removeFavouriteFriend(self, nsa_id: int):
        """Remove favourite friend."""
        resp = requests.post(
            url=self.url + "/v3/Friend/Favorite/Delete",
            headers=self.headers,
            json={"parameter": {"nsaId": nsa_id}},
        )
        if resp.status_code != 200:
            raise Exception(f"Error: {resp.status_code}")
        return resp.json()

    def getToken(self):
        parameters = {
            "parameter": {
                "naBirthday": self.user_info["birthday"],
                "timestamp": self.NSOL.flapg["timestamp"],
                "f": self.NSOL.flapg["f"],
                "requestId": self.NSOL.flapg["uuid"],
                "naIdToken": self.token["id_token"],
            }
        }
        resp = requests.post(
            url=self.url + "/v3/Account/GetToken",
            headers=self.headers,
            json=parameters,
        )
        if resp.status_code != 200:
            raise Exception(f"Error: {resp.status_code}")
        return resp.json()

    def sync_login(self):
        wasc_access_token = keyring.get_password("nso-bridge", "login")
        wasc_time = keyring.get_password("nso-bridge", "wasc_time")

        if wasc_time is None:
            wasc_time = 0.0
        if wasc_access_token is not None:
            self.login = pickle.loads(
                base64.b64decode(wasc_access_token.encode("utf-8"))
            )
            self.headers[
                "Authorization"
            ] = f"Bearer {self.login['login']['result']['webApiServerCredential']['accessToken']}"

        if time.time() - int(float(wasc_time)) < 7170:
            return

        login = self.NSOL.to_account()
        self.login = {
            "login": login,
            "time": time.time(),
        }
        self.headers[
            "Authorization"
        ] = f"Bearer {self.login['login']['result']['webApiServerCredential']['accessToken']}"
        keyring.set_password(
            "nso-bridge",
            "login",
            base64.b64encode(pickle.dumps(self.login)).decode("utf-8"),
        )
        keyring.set_password(
            "nso-bridge",
            "wasc_access_token",
            self.login["login"]["result"]["webApiServerCredential"]["accessToken"],
        )
        keyring.set_password("nso-bridge", "wasc_time", str(self.login["time"]))
