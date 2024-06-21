from typing import Union

from pydantic import BaseModel


class RequestResponseBase(BaseModel):
    request_url: str
    request_type: str
    request_body: Union[str, dict]
    request_headers: Union[str, dict]
    request_params: str
    response_data: Union[str, dict]
    response_status_code: int
    response_type: str

class RequestBase(BaseModel):
    request_url: str
    request_type: str
    request_body: Union[str, dict]
    request_headers: Union[str, dict]
    request_params: str

class RequestCreate(RequestBase):
    pass


class Request(RequestBase):
    id: int
    unique_id: str

    class Config:
        from_attributes = True
