from fastapi.encoders import jsonable_encoder
import hashlib
import json
from app.schemas import RequestCreate
from app.database import database



def get_requests(skip: int = 0, limit: int = 10):
    collection = database['configuration']
    cursor = collection.find().skip(skip).limit(limit)
    return list(cursor)


def create_request(request: RequestCreate):

    request_body = json.dumps(request.request_body) if isinstance(request.request_body, dict)\
        else request.request_body
    request_headers = json.dumps(request.request_headers) if isinstance(request.request_headers, dict)\
        else request.request_headers

    unique_id = hashlib.sha256((request.request_url + request.request_type + request_body +
                                request_headers + request.request_params).encode()).hexdigest()
    request_dict = jsonable_encoder(request)

    # Check if a request with the same unique_id already exists
    collection = database['configuration']
    existing_request = collection.find_one({"unique_id": unique_id})
    if existing_request:
        return existing_request  # Return existing data if found

    # If not found, create a new request
    request_dict['unique_id'] = unique_id
    collection.insert_one(request_dict)
    return request_dict


def get_mocked_response(request: RequestCreate):
    request_body = json.dumps(request.request_body) if isinstance(request.request_body, dict) \
        else request.request_body
    request_headers = json.dumps(request.request_headers) if isinstance(request.request_headers, dict) \
        else request.request_headers

    unique_id = hashlib.sha256((request.request_url + request.request_type + request_body +
                                request_headers + request.request_params).encode()).hexdigest()

    # Check if a request with the same unique_id already exists
    collection = database['configuration']
    existing_request = collection.find_one({"unique_id": unique_id})

    if not existing_request:
        return "data is not present"  # Return existing data if found
    else:
        return json.loads(existing_request.get("request_body")) if isinstance(existing_request.get("request_body"), str)\
            else existing_request.get("request_body")

