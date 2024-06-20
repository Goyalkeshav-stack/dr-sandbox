from pydantic import BaseModel


class RequestBase(BaseModel):
    url: str
    request_type: str
    request_body: str
    request_parameter: str
    request_response: str
    response_status: int


class RequestCreate(RequestBase):
    pass


class Request(RequestBase):
    id: int
    unique_id: str

    class Config:
        orm_mode = True
