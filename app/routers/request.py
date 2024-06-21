import json

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from starlette.responses import JSONResponse

from .. import crud, schemas
from ..database import SessionLocal, engine
from ..models import Base
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
        request_url = model_data["url"]
        request_type = model_data["request_type"]
        request_body = json.dumps(model_data["request_payload"])
        request_headers = model_data["request_headers"]
        request_params = model_data["request_params"]
        response_data = model_data["response_data"]
        response_status_code = model_data["response_status_code"]
        response_type = model_data["response_type"]

        hash = hashlib.new('sha256')
        hash_key = request_url + request_type + json.dumps(request_body) + json.dumps(request_headers) + request_params
        hash.update(hash_key.encode())

        req = RequestModel()
        req.init_model()
        req.url = request_url
        req.request_type = request_type
        req.request_body = request_body
        req.request_parameter = request_params
        req.request_headers = request_headers
        req.unique_id = hash.hexdigest()
        req.request_response = response_data
        req.response_type = response_type
        req.response_status = response_status_code

        db.add(req)
        db.commit()
        return JSONResponse("Data inserted successfully")
    except Exception as exc:
        return JSONResponse("Data insertion Failed")


@router.post("/fetch-response")
def fetch_response(payload: schemas.RequestBase, db: Session = Depends(get_db())):
    try:
        model_data = payload.model_dump()
        request_url = model_data["url"]
        request_type = model_data["request_type"]
        request_body = json.dumps(model_data["request_payload"])
        request_headers = model_data["request_headers"]
        request_params = model_data["request_params"]

        hash = hashlib.new('sha256')
        hash_key = request_url + request_type + json.dumps(request_body) + json.dumps(request_headers) + request_params
        hash.update(hash_key.encode())

        unique_id = hash.hexdigest()
        res = RequestModel()
        result = db.query(res).filter(unique_id)
        res.modelmapper(result)

        return JSONResponse(res, "Data Fetched successfully")
    except Exception as exc:
        return JSONResponse("Data Fetch Failed")

@router.post("/requests/", response_model=schemas.Request)
def create_request(request: schemas.RequestCreate, db: Session = Depends(get_db)):
    print("here in create", request)
    return crud.create_request(db=db, request=request)
