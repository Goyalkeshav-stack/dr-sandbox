from pydantic import BaseModel


class RequestResponseBase(BaseModel):
    url: str
    request_type: str
    request_payload: dict
    request_headers: dict
    request_params: str
    response_data: dict
    response_status_code: int
    response_type: str

class RequestBase(BaseModel):
    url: str
    request_type: str
    request_payload: dict
    request_headers: dict
    request_params: str
    response_data: dict
    response_status_code: int
    response_type: str

class RequestCreate(RequestBase):
    pass


class Request(RequestBase):
    id: int
    unique_id: str

    class Config:
        orm_mode = True
