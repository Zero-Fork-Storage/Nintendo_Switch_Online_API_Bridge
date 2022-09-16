import keyring

from nso_bridge.nsa import NintendoSwitchAccount
from nso_bridge.nso import NintendoSwitchOnlineAPI


def test_get_nso_app_version():
    try:
        app = NintendoSwitchAccount()
        app.get_nso_app_version()
        assert True
    except Exception:
        assert False


def test_nso_login():
    try:
        app = NintendoSwitchAccount()

        # override the nso_app_version
        app.nso_app_version = app.get_nso_app_version()
        session_token = keyring.get_password("nso-bridge", "session_token")

        nso_res = NintendoSwitchOnlineAPI(
            nso_app_version=app.nso_app_version,
            session_token=session_token,
        )
        nso_res.sync_login()
        assert True
    except Exception:
        assert False


def test_getAnnouncements():
    try:
        app = NintendoSwitchAccount()

        # override the nso_app_version
        app.nso_app_version = app.get_nso_app_version()
        session_token = keyring.get_password("nso-bridge", "session_token")

        nso_res = NintendoSwitchOnlineAPI(
            nso_app_version=app.nso_app_version,
            session_token=session_token,
        )
        nso_res.sync_login()
        nso_res.getAnnouncements()
        assert True
    except Exception:
        assert False


def test_getFriends():
    try:
        app = NintendoSwitchAccount()

        # override the nso_app_version
        app.nso_app_version = app.get_nso_app_version()
        session_token = keyring.get_password("nso-bridge", "session_token")

        nso_res = NintendoSwitchOnlineAPI(
            nso_app_version=app.nso_app_version,
            session_token=session_token,
        )
        nso_res.sync_login()
        nso_res.getFriends()
        assert True
    except Exception:
        assert False


def test_getWebServices():
    try:
        app = NintendoSwitchAccount()

        # override the nso_app_version
        app.nso_app_version = app.get_nso_app_version()
        session_token = keyring.get_password("nso-bridge", "session_token")

        nso_res = NintendoSwitchOnlineAPI(
            nso_app_version=app.nso_app_version,
            session_token=session_token,
        )
        nso_res.sync_login()
        nso_res.getWebServices()
        assert True
    except Exception:
        assert False


def test_getActiveEvent():
    try:
        app = NintendoSwitchAccount()

        # override the nso_app_version
        app.nso_app_version = app.get_nso_app_version()
        session_token = keyring.get_password("nso-bridge", "session_token")

        nso_res = NintendoSwitchOnlineAPI(
            nso_app_version=app.nso_app_version,
            session_token=session_token,
        )
        nso_res.sync_login()
        nso_res.getActiveEvent()
        assert True
    except Exception:
        assert False


def test_getEvent():
    try:
        app = NintendoSwitchAccount()

        # override the nso_app_version
        app.nso_app_version = app.get_nso_app_version()
        session_token = keyring.get_password("nso-bridge", "session_token")

        nso_res = NintendoSwitchOnlineAPI(
            nso_app_version=app.nso_app_version,
            session_token=session_token,
        )
        nso_res.sync_login()
        nso_res.getEvent()
        assert True
    except Exception:
        assert False


def test_getUser():
    try:
        app = NintendoSwitchAccount()

        # override the nso_app_version
        app.nso_app_version = app.get_nso_app_version()
        session_token = keyring.get_password("nso-bridge", "session_token")

        nso_res = NintendoSwitchOnlineAPI(
            nso_app_version=app.nso_app_version,
            session_token=session_token,
        )
        nso_res.sync_login()
        nso_res.getUser()
        assert True
    except Exception:
        assert False


def test_getCurrentUser():
    try:
        app = NintendoSwitchAccount()

        # override the nso_app_version
        app.nso_app_version = app.get_nso_app_version()
        session_token = keyring.get_password("nso-bridge", "session_token")

        nso_res = NintendoSwitchOnlineAPI(
            nso_app_version=app.nso_app_version,
            session_token=session_token,
        )
        nso_res.sync_login()
        nso_res.getCurrentUser()
        assert True
    except Exception:
        assert False


def test_getFriendCodeUrl():
    try:
        app = NintendoSwitchAccount()

        # override the nso_app_version
        app.nso_app_version = app.get_nso_app_version()
        session_token = keyring.get_password("nso-bridge", "session_token")

        nso_res = NintendoSwitchOnlineAPI(
            nso_app_version=app.nso_app_version,
            session_token=session_token,
        )
        nso_res.sync_login()
        nso_res.getFriendCodeUrl()
        assert True
    except Exception:
        assert False


def test_getCurrentUserPermissions():
    try:
        app = NintendoSwitchAccount()

        # override the nso_app_version
        app.nso_app_version = app.get_nso_app_version()
        session_token = keyring.get_password("nso-bridge", "session_token")

        nso_res = NintendoSwitchOnlineAPI(
            nso_app_version=app.nso_app_version,
            session_token=session_token,
        )
        nso_res.sync_login()
        nso_res.getCurrentUserPermissions()
        assert True
    except Exception:
        assert False
