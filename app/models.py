from sqlalchemy import Column, Integer, String, Text
from .database import Base


class RequestModel(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    unique_id = Column(String, unique=True, index=True)
    url = Column(String, index=True)
    request_type = Column(String)
    request_body = Column(Text)
    request_parameter = Column(Text)
    request_response = Column(Text)
    response_status = Column(Integer)
