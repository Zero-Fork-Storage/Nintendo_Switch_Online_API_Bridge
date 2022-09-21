from pydantic import BaseModel


class ErrorResponse(BaseModel):
    status: int
    errorMessage: str | None
    correlationId: str


class Response(BaseModel):
    status: int
    result: dict | None
    correlationId: str
