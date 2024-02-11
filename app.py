# app.py
from flask import Flask
from utils.backtesting import run_backtest
from websockets.kraken_websocket import run_kraken_websocket
from strategies.sma_strategy import simple_ma_strategy
from datarequests.get_historic_data import get_historic_data
from indicators.sma import calculate_moving_average

def create_app():
    app = Flask(__name__)

    @app.route("/")
    def hello():
        return app.send_static_file("index.html")
    @app.route("/backtest")
    def backtest():
        start_date = " 01 Jan 2022 00:00:00"
        end_date = " 01 Feb 2022 23:59:59"
        raw_data = get_historic_data(symbol='BTCUSDT', interval='1m', start_str=start_date.strip(), end_str=end_date.strip())        
        formatted_data = [{
            'timestamp': data_point[0],
            'open': float(data_point[1]),
            'high': float(data_point[2]),
            'low': float(data_point[3]),
            'close': float(data_point[4]),
        } for data_point in raw_data]
        
        trades = run_backtest(simple_ma_strategy, formatted_data)        
        print(trades)    
        return app.send_static_file("index.html")

        

    return app


if __name__ == "__main__":
    # Start the WebSocket client in a background thread
  #  ws_thread = threading.Thread(target=run_kraken_websocket)
  #  ws_thread.start()

    # Start the Flask application
    flask_app = create_app()
    flask_app.run(host="0.0.0.0", port=9000, use_reloader=False)  # use_reloader=False to prevent duplicate threads
