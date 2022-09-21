from pydantic import BaseModel


class ResponseMessageModel(BaseModel):
    message: str
