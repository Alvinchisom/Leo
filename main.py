#main.py
from fastapi import  FastAPI
from routes.user import route

app = FastAPI()

app.include_router(route)