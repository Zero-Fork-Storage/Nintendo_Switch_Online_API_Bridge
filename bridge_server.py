import time
import json
import keyring
import base64
import pickle
from app.nsa import NintendoSwitchAccount
from app.nso import NintendoSwitchOnlineAPI

app = NintendoSwitchAccount()

# override the nso_app_version
app.nso_app_version = "2.1.1"
session_token = keyring.get_password("nso-bridge", "session_token")


nso_res = NintendoSwitchOnlineAPI(
    nso_app_version=app.nso_app_version,
    session_token=session_token,
)
nso_res.sync_login()
print(json.dumps(nso_res.getFriends(), indent=4, ensure_ascii=False))

