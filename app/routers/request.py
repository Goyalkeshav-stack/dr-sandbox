import json

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from .. import crud, schemas
from ..database import SessionLocal, engine
from ..models import Base, AlchemyEncoder
from typing_extensions import List
import hashlib
from ..models import RequestModel
Base.metadata.create_all(bind=engine)

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("/requests/", response_model=List[schemas.Request])
def read_requests(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    requests = crud.get_requests(db, skip=skip, limit=limit)
    return requests


@router.post("/publish-response")
def publish_response(payload: schemas.RequestResponseBase, db: Session = Depends(get_db())):
    try:
        model_data = payload.model_dump()
        request_url = model_data["request_url"]
        request_type = model_data["request_type"]
        request_body = json.dumps(model_data["request_body"])
        request_headers = model_data["request_headers"]
        request_params = model_data["request_params"]

        hash = hashlib.new('sha256')
        hash_key = request_url + request_type + json.dumps(request_body) + json.dumps(request_headers) + request_params
        hash.update(hash_key.encode())
        unique_id = hash.hexdigest()
        model_data["unique_id"] = unique_id

        request_input = RequestInput(model_data)
        request = modelmapper(request_input)
        db.add(request)
        db.commit()
        return JSONResponse("Data inserted successfully")
    except Exception as exc:
        return JSONResponse("Data insertion Failed")


@router.post("/fetch-response")
def fetch_response(payload: schemas.RequestBase, db: Session = Depends(get_db())):
    try:
        model_data = payload.model_dump()
        request_url = model_data["request_url"]
        request_type = model_data["request_type"]
        request_body = json.dumps(model_data["request_body"])
        request_headers = model_data["request_headers"]
        request_params = model_data["request_params"]

        hash = hashlib.new('sha256')
        hash_key = request_url + request_type + json.dumps(request_body) + json.dumps(request_headers) + request_params
        hash.update(hash_key.encode())

        unique_id = hash.hexdigest()

        result_query = db.query(RequestModel).filter(RequestModel.unique_id == unique_id)
        retval = result_query.all()
        retval = json.dumps(retval, cls=AlchemyEncoder)

        return JSONResponse(retval, 200)
    except Exception as exc:
        return JSONResponse("Data Fetch Failed", 200)

@router.post("/requests/", response_model=schemas.Request)
def create_request(request: schemas.RequestCreate, db: Session = Depends(get_db)):
    print("here in create", request)
    return crud.create_request(db=db, request=request)


def modelmapper(req):
    request = RequestModel()
    request.id = req.id
    request.unique_id = req.unique_id
    request.url = req.url
    request.request_type = req.request_type
    request.request_body = req.request_body
    request.request_parameter = req.request_parameter
    request.request_response = req.request_response
    request.response_status = req.response_status
    return request


class RequestInput:
    """
    TaxRates input class for post method
    """
    def __init__(self, params):
        self.unique_id = params.get("unique_id")
        self.url = params.get("url")
        self.request_type = params.get("request_type")
        self.request_body = params.get("request_body")
        self.request_headers = params.get("request_headers")
        self.request_parameter = params.get("request_parameter")
        self.request_response = params.get("request_response")
        self.response_status = params.get("response_status")
        self.response_type = params.get("response_type")
