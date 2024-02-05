import requests
import datetime

def get_binance_historic_klines(symbol='BTCUSDT', interval='1m', start_str=None, end_str=None):
    """
    Retrieves historic Kline data from Binance for a specified symbol and time interval.

    Parameters:
        symbol (str): The trading pair symbol (default is 'BTCUSDT').
        interval (str): The time interval for the Kline data (default is '1m').
        start_str (str): The start time in string format (optional).
        end_str (str): The end time in string format (optional).

    Returns:
        dict: The historic Kline data in JSON format.
    """
    url = 'https://api.binance.com/api/v3/klines'
    params = {
        'symbol': symbol,
        'interval': interval,
        'limit': 1000  # Max allowed by Binance
    }
    
    if start_str:
        params['startTime'] = int(datetime.datetime.strptime(start_str, "%d %b %Y %H:%M:%S").timestamp() * 1000)
    
    if end_str:
        params['endTime'] = int(datetime.datetime.strptime(end_str, "%d %b %Y %H:%M:%S").timestamp() * 1000)
    
    response = requests.get(url, params=params)
    data = response.json()
    return data

# Example usage:
start_str = "01 Jan 2021 00:00:00"
end_str = "01 Feb 2021 00:00:00"
klines = get_binance_historic_klines('BTCUSDT', '1m', start_str, end_str)

for kline in klines[:5]:  # Print first 5 entries
    open_time = datetime.datetime.fromtimestamp(kline[0] / 1000)
    print(f"Open Time: {open_time}, Open: {kline[1]}, High: {kline[2]}, Low: {kline[3]}, Close: {kline[4]}")
