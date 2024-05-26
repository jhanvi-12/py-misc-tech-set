"""This module is responsible to define the API endpoint for websocket."""
from fastapi import WebSocket, APIRouter
from loguru import logger

router = APIRouter()

@router.websocket("/ws")
async def connect_websocket(websocket: WebSocket):
    """This API endpoint is used to connect to a websocket server."""
    # It accepts thw websocket connections and allows bidirectional communication.
    await websocket.accept()
    logger.info("====> Connected to the socket server")
    while True:
        # Continuously receive incoming message from server.
        data = await websocket.receive_text()
        try:
            await websocket.send_text(f"You send:- {data}")
            logger.info(f"<==== Received message from server {data}")
        except Exception:
            await websocket.send_text("Error sending message to websocket server.")
            logger.error("<==== Error sending message to websocket server")
