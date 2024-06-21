from fastapi import FastAPI
from app.schemas import RequestModel, MockRequest, MockResponse
from app.crud import *
from typing import List


app = FastAPI()


@app.post("/publish-response", response_model=RequestModel)
def create_new_request(request: RequestCreate):
    # request_dict = jsonable_encoder(request)
    return create_request(request)


@app.get("/fetch-all-requests", response_model=List[RequestModel])
def read_requests(skip: int = 0, limit: int = 10):
    requests = get_requests(skip=skip, limit=limit)
    return requests


@app.post("/fetch-response")
def create_new_request(request: MockRequest):
    return get_mocked_response(request)
