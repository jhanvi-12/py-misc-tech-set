"""This module is used run fastapi server and is responsible for running the server."""
import uvicorn
import config
from __init__ import app

if __name__ == "__main__":
    uvicorn.run("run:app", port=int(config.SERVER_PORT),
                 host=config.SERVER_HOST, reload=True)
