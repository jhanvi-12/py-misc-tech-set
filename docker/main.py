"""This module is used to run docker to print something"""
from fastapi import FastAPI
import uvicorn

app = FastAPI(title="Welcome to fastapi application with docker")

@app.get("/demo")
def hello():
    "This API is used to display simple message."
    data = {"success": "Hello, there! Welcome to the first docker program."}
    return data


if __name__ == "__main__":
    uvicorn.run(app, port=8005, host="0.0.0.0")