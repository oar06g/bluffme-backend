from fastapi import FastAPI
from .api_v1 import BluffMe

app = FastAPI()

app.include_router(BluffMe().router)
