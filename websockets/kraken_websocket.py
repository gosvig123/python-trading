# Corrected import statements
from websocket._app import WebSocketApp
import json
def on_message(ws, message) -> None:
    print("Message received:")
    print(json.loads(message))

def on_error(ws, error) -> None:
    print("Error:")
    print(error)

def on_close(ws, close_status_code, close_msg) -> None:
    print("WebSocket closed:")
    print(f"Code: {close_status_code}, Message: {close_msg}")

def on_open(ws) -> None:
    subscribe_to_ohlc = {
        "event": "subscribe",
        "pair": ["XBT/EUR"],
        "subscription": {
            "name": "ticker"
        }
    }
    ws.send(json.dumps(subscribe_to_ohlc))

def run_kraken_websocket():
    ws_app = WebSocketApp("wss://ws.kraken.com",
                          on_open=on_open,
                          on_message=on_message,
                          on_error=on_error,
                          on_close=on_close)
    ws_app.run_forever()
