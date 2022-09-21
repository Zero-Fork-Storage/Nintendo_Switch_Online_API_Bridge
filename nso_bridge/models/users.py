from pydantic import BaseModel

from nso_bridge.models.accounts import _friendCode, _user
from nso_bridge.models.response import Response


class _active_(BaseModel):
    active: bool


class _active(BaseModel):
    active: _active_


class _membership(BaseModel):
    membership: _active


class _current_user_link(BaseModel):
    nintendoAccount: _membership
    friendCode: _friendCode


class _current_user(_user):
    links: _current_user_link


class CurrentUser(Response):
    result: _current_user | None
