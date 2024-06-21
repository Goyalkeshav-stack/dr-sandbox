from pydantic import BaseModel
from typing import Any


# Define Pydantic models
class RequestCreate(BaseModel):
    request_url: str
    request_type: str
    request_body: Any
    request_headers: Any
    request_params: str


class RequestModel(RequestCreate):
    unique_id: str


class MockRequest(BaseModel):
    request_url: str
    request_type: str
    request_body: Any
    request_headers: Any
    request_params: str


class MockResponse(BaseModel):
    request_body: Any

