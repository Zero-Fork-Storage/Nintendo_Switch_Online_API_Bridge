import keyring

from nso_bridge.nsa import NintendoSwitchAccount
from nso_bridge.nso import NintendoSwitchOnlineAPI


def test_nso_login():
    try:
        app = NintendoSwitchAccount()

        # override the nso_app_version
        app.nso_app_version = '2.1.1'
        session_token = keyring.get_password("nso-bridge", "session_token")

        nso_res = NintendoSwitchOnlineAPI(
            nso_app_version=app.nso_app_version,
            session_token=session_token,
        )
        nso_res.sync_login()
        assert True
    except Exception:
        assert False