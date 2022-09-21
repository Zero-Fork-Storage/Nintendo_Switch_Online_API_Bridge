from pydantic import BaseModel, Field

from nso_bridge.models.accounts import _presence
from nso_bridge.models.response import Response


class _friend(BaseModel):
    _id: int = Field(..., alias="id")
    nsaId: str
    imageUri: str
    name: str
    isFriend: bool
    isFavoriteFriend: bool
    isServiceUser: bool
    friendCreatedAt: int
    presence: _presence


class _friends(BaseModel):
    friends: list[_friend]


class Friends(Response):
    result: _friends | None


class _friendCode(BaseModel):
    friendCode: str
    url: str


class FriendCode(Response):
    result: _friendCode | None
