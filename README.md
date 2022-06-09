# Nintendo Switch Online API Bridge

NINTENDO SWITCH ONLINE API BRIDGE

## What is it?

Nintendo Switch Online API Bridge is a simple wrapper. It allows you to easily access the API and get the data you need.

## Installation

```bash
pip install git+https://github.com/zeroday0619/Nintendo_Switch_Online_API_Bridge.git
```

## Example Code

### GetSelf

Get information of My Nintendo Switch Account.

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
print(json.dumps(nso_res.getSelf(), indent=4, ensure_ascii=False))

```

### GetFriends

Get information of friends registered to Nintendo Switch account.

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
