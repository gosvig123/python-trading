# app.py
from flask import Flask
from pandas import DataFrame
import threading
from websockets.kraken_websocket import run_kraken_websocket
from datarequests.get_historic_data import kline
def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return app.send_static_file("index.html")
    @app.route("/backtest")
    def backtest():
       return print(kline)

        

    return app


if __name__ == "__main__":
    # Start the WebSocket client in a background thread
  #  ws_thread = threading.Thread(target=run_kraken_websocket)
  #  ws_thread.start()

    # Start the Flask application
    flask_app = create_app()
    flask_app.run(host="0.0.0.0", port=9000, use_reloader=False)  # use_reloader=False to prevent duplicate threads
