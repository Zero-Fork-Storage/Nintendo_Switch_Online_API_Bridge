from re import U
from tkinter import W
import keyring
import base64
import pickle
from app.nsa import NintendoSwitchAccount
from app.nso import NintendoSwitchOnlineAPI

app = NintendoSwitchAccount()

# override the nso_app_version
app.nso_app_version = "2.1.1"
session_token = keyring.get_password("nso-bridge", "session_token")
wasc_access_token = keyring.get_password("nso-bridge", "login")
wasc_time = keyring.get_password("nso-bridge", "wasc_time")

if wasc_access_token is not None and wasc_time is not None:
    login = pickle.loads(base64.b64decode(wasc_access_token.encode('utf-8')))
    service_token = app.get_service_token(session_token)
    user_info = app.get_user_info(service_token['access_token'])
    nso_res = NintendoSwitchOnlineAPI(
        nso_app_version=app.nso_app_version,
        user_info=user_info,
        service_token=service_token,
    )

    nso_res.sync_login()
    print(nso_res.getSelf())
    print(nso_res.getFriends())
else:
    session_token = app.nso_login(app.m_input)
    service_token = app.get_service_token(session_token)
    user_info = app.get_user_info(service_token['access_token'])
    nso_res = NintendoSwitchOnlineAPI(
        nso_app_version=app.nso_app_version,
        user_info=user_info,
        service_token=service_token,
    )

    nso_res.sync_login()
    print(nso_res.getSelf())
    print(nso_res.getFriends())