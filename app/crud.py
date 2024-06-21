from sqlalchemy.orm import Session
from app.models import RequestModel
import hashlib
from app.schemas import RequestCreate


def get_requests(db: Session, skip: int = 0, limit: int = 10):
    return db.query(RequestModel).offset(skip).limit(limit).all()


def create_request(db: Session, request: RequestCreate):
    unique_id = hashlib.sha256((request.url + request.request_type).encode()).hexdigest()

    # Check if a request with the same unique_id already exists
    existing_request = db.query(RequestModel).filter(RequestModel.unique_id == unique_id).first()
    if existing_request:
        return existing_request# Return existing data if found

    # If not found, create a new request
    db_request = RequestModel(**request.dict(), unique_id=unique_id)
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request
