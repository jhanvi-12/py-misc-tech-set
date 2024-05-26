from fastapi import FastAPI
from view import router

app = FastAPI(title="Welcome to the websocket server.")

app.include_router(router)