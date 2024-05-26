# WebSocket Integration with FastAPI and Python

[![WebSocket](https://img.shields.io/badge/WebSocket-Supported-brightgreen)](https://en.wikipedia.org/wiki/WebSocket)


This repository demonstrates how to integrate WebSocket functionality into a FastAPI application using Python.

## What is WebSocket?

WebSocket is a communication protocol that provides full-duplex communication channels over a single, long-lived connection between a client and a server. Unlike traditional HTTP connections, which are stateless and require multiple connections for ongoing communication, WebSocket allows for real-time, bidirectional communication between clients and servers.

## Uses of WebSocket

WebSocket is commonly used in scenarios that require real-time data transfer or continuous communication between clients and servers. Some common use cases include:

- Chat applications
- Real-time notifications
- Live updates (e.g., stock tickers, sports scores)
- Multiplayer online games
- Collaborative editing tools
- Remote control applications

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/yourrepository.git
```

2. Navigate to the project directory:
```bash
cd yourrepository
```

3. Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

4. Websocket router code snippets
```python
from fastapi import WebSocket, APIRouter

router = APIRouter()

@router.websocket("/ws")
async def connect_websocket(websocket: WebSocket):
    """This API endpoint is used to connect to a websocket server."""
    # It accepts thw websocket connections and allows bidirectional communication.
    await websocket.accept()
    print("[INFO] =====> Connected to the socket server")
    while True:
        # Continuously receive incoming message from server.
        data = await websocket.receive_text()
        try:
            await websocket.send_text(f"You send:- {data}")
        except Exception:
            await websocket.send_text("Error sending message to websocket server.")
```

## Running the Server
1. Open the first terminal.
2. Navigate to the directory containing the server.py file (Here we have run.py file as server file).
3. Run the following command to start the server:
```bash
python run.py
```

## Requested websocket API endpoint from postman
1. Connecting to the websocket server {ws://localhost:8004/ws}.
2. Request data from postman.
```bash
{
    "data": "Hello, world"
}
or
"Hello, world"
```
3. You will recieve the response from the websocket server.