from app.nsa import NintendoSwitchAccount
from app.nso import NintendoSwitchOnlineAPI

app = NintendoSwitchAccount()

# override the nso_app_version
app.nso_app_version = app.get_nso_app_version()

service_token = app.nso_login()
res = app.get_service_token(service_token)
user_info = app.get_user_info(res["access_token"])
nso_res = NintendoSwitchOnlineAPI(
    nso_app_version=app.nso_app_version,
    user_info=user_info,
    service_token=res,
)
nso_res.sync_login()
print(nso_res.login)