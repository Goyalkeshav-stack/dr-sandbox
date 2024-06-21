# dr-sandbox
This repo contains a generic server configuration that will be helpful in feature development by providing mock data responses for the API calls

Step1: pip install -r requirements

step2: uvicorn app.main:app --reload


step3: For create request use bellow curl in postman
curl --location --request POST 'http://127.0.0.1:8000/requests' \
--header 'Content-Type: application/json' \
--data-raw '{
    "url":"http://example4.com",
            "request_type":"GET",
            "request_body":"{}",
            "request_parameter":"{}",
            "request_response":"{}",
            "response_status":200
}'
