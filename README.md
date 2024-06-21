# dr-sandbox
This repo contains a generic server configuration that will be helpful in feature development by providing mock data responses for the API calls

Step1: pip install -r requirements

step2: uvicorn app.main:app --reload


step3: For create request use bellow curl in postman
curl --location --request POST 'http://127.0.0.1:8000/publish-response' \
--header 'Content-Type: application/json' \
--data-raw '{
    "request_url": "/mashup/testingaccdityaprogramsbatch",
    "request_type": "GET",
    "request_body": "{}",
    "request_headers": "{}",
    "request_params": "{}",
    "request_response": "{}",
    "response_status_code": 200,
    "response_data": "{}",
    "response_type": ""
}'

Step4: For fetch all request inside the collection 

curl --location --request GET 'http://127.0.0.1:8000/fetch-all-requests' \
--data-raw ''


Step5: getting specific response of existing request with end point
curl --location --request POST 'http://127.0.0.1:8000/fetch-response' \
--header 'Content-Type: application/json' \
--data-raw '{
    "request_url": "/mashup/lenderprogramsbatch",
    "request_type": "GET",
    "request_body": {"response": "empty response for testing"},
    "request_headers": "{}",
    "request_params": "{}",
    "request_response": "{}",
    "response_status_code": 200,
    "response_data": "{}",
    "response_type": ""
}'