from sqlalchemy.orm import Session
from .models import RequestModel


def get_requests(db: Session, skip: int = 0, limit: int = 10):
    return db.query(RequestModel).offset(skip).limit(limit).all()
