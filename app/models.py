from sqlalchemy import Column, Integer, String, Text
from app.database import Base

class RequestModel(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    unique_id = Column(String, unique=True, index=True)
    url = Column(String, index=True)
    request_type = Column(String)
    request_body = Column(Text)
    request_headers = Column(Text)
    request_parameter = Column(Text)
    request_response = Column(Text)
    response_status = Column(Integer)
    response_type = Column(Text)

    def init_model(self):
        self.id = None
        self.unique_id = None
        self.url = None
        self.request_type = ""
        self.request_body = {}
        self.request_headers = {}
        self.request_parameter = ""
        self.request_response = {}
        self.response_status = ""
        self.response_type = ""


    def modelmapper(self, req):
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