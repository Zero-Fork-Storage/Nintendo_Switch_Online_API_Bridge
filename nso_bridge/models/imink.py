from pydantic import BaseModel


class Imink(BaseModel):
    f: str
    request_id: str
    timestamp: int
