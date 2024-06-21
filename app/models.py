import decimal
from datetime import date
from json import JSONEncoder, dumps

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import DeclarativeMeta

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

class AlchemyEncoder(JSONEncoder):
    def specialTypesEncoder(obj):
        """JSON encoder function for SQLAlchemy special classes."""
        if isinstance(obj, date):
            return obj.isoformat()
        elif isinstance(obj, decimal.Decimal):
            return float(obj)

    def default(self, obj):
        if isinstance(obj.__class__, DeclarativeMeta):
            # an SQLAlchemy class
            fields = {}
            for field in [x for x in dir(obj) if not x.startswith("_") and x != "metadata"]:
                data = obj.__getattribute__(field)
                try:
                    if isinstance(data, date):
                        fields[field] = data.isoformat()
                    elif isinstance(data, decimal.Decimal):
                        fields[field] = float(data)
                    else:
                        dumps(data)  # this will fail on non-encodable values, like other classes
                        fields[field] = data
                except TypeError:
                    fields[field] = None
            # a json-encodable dict
            return fields
        return JSONEncoder.default(self, obj)