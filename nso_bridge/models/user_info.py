from pydantic import BaseModel, Field


class _internalAnalysis(BaseModel):
    permitted: bool
    updatedAt: int


class _targetMarketing(BaseModel):
    updatedAt: int
    permitted: bool


class _analyticsPermissions(BaseModel):
    internalAnalysis: _internalAnalysis
    targetMarketing: _targetMarketing


class _timezone(BaseModel):
    _id: str = Field(..., alias="id")
    name: str
    utcOffsetSeconds: int
    utcOffset: str


class _deals(BaseModel):
    optedIn: bool
    updatedAt: int


class _survey(BaseModel):
    optedIn: bool
    updatedAt: int


class _eachEmailOptedIn(BaseModel):
    deals: _deals
    survey: _survey


class UserInfo(BaseModel):
    _id: str = Field(..., alias="id")
    mii: None
    candidateMiis: list
    region: None
    gender: str
    language: str
    country: str
    birthday: str
    isChild: bool
    nickname: str
    screenName: str
    createdAt: int
    updatedAt: int
    emailOptedIn: bool
    emailVerified: bool
    emailOptedInUpdatedAt: int
    analyticsOptedIn: bool
    analyticsOptedInUpdatedAt: int
    clientFriendsOptedIn: bool
    clientFriendsOptedInUpdatedAt: int
    timezone: _timezone
    analyticsPermissions: _analyticsPermissions
    eachEmailOptedIn: _eachEmailOptedIn | None
