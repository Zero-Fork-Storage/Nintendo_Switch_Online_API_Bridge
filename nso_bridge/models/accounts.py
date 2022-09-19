from typing import Optional

from pydantic import BaseModel, Field


class _friendCode(BaseModel):
    regenerable: bool
    regenerableAt: int
    _id: str = Field(..., alias="id")


class _membership(BaseModel):
    active: bool


class _nintendoAccount(BaseModel):
    membership: _membership


class _links(BaseModel):
    nintendoAccount: _nintendoAccount
    friendCode: _friendCode


class _permissions(BaseModel):
    presence: str


class _presence(BaseModel):
    state: str
    updatedAt: int
    logoutAt: int
    game: dict


class _user(BaseModel):
    _id: int = Field(..., alias="id")
    nsaId: str
    imageUri: str
    name: str
    supportId: str
    isChildRestricted: bool
    etag: str
    links: _links
    permissions: _permissions
    presence: _presence


class _webApiServerCredential(BaseModel):
    accessToken: str
    expiresIn: int


class _firebaseCredential(BaseModel):
    accessToken: str
    expiresIn: int


class _accounts(BaseModel):
    user: _user
    webApiServerCredential: _webApiServerCredential
    firebaseCredential: _firebaseCredential


class Accounts(BaseModel):
    status: int
    result: Optional[_accounts]
    errorMessage: Optional[str]
    correlationId: str


class Login(BaseModel):
    login: Accounts | None
    time: float


class ServiceToken(BaseModel):
    expires_in: int
    id_token: str
    access_token: str
    scope: list[str]
    token_type: str
