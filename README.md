# Nintendo_Switch_Online_API_Bridge

NINTENDO SWITCH ONLINE API BRIDGE

## Example

### Friends

```python
import json
import keyring

from nso_bridge.nsa import NintendoSwitchAccount
from nso_bridge.nso import NintendoSwitchOnlineAPI

import logging

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

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
```
