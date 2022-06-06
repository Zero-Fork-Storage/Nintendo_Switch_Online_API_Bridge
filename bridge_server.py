from app.nso import NintendoSwitchAccount

app = NintendoSwitchAccount()

# override the nso_app_version
app.nso_app_version = app.get_nso_app_version()

service_token = app.nso_login()
res = app.get_service_token(service_token)
