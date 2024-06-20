from fastapi import FastAPI
from .routers import request

app = FastAPI()

app.include_router(request.router)
