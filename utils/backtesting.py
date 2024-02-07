def backtest(strategy, data):
    """
    Backtests a trading strategy on a provided dataset.

    Parameters:
    - strategy: A function that takes a slice of data and returns a trading signal ('buy', 'sell', or 'hold').
    - data: A list of dictionaries, each representing the market data at a point in time.

    Returns:
    - A dictionary with the backtest results including total profit, percentage profit, and a list of trades.
    """
    balance = 0
    position = 0
    trades = []

    for i in range(len(data)):
        signal = strategy(data[:i+1])
        price = data[i]['close']
        
        if signal == 'buy' and balance >= price:
            position += balance / price
            balance = 0
            trades.append({'action': 'buy', 'price': price, 'timestamp': data[i]['timestamp']})
        
        elif signal == 'sell' and position > 0:
            balance += position * price
            position = 0
            trades.append({'action': 'sell', 'price': price, 'timestamp': data[i]['timestamp']})

    # If there is an open position, close it at the last price
    if position > 0:
        balance += position * data[-1]['close']
        position = 0
        trades.append({'action': 'sell', 'price': data[-1]['close'], 'timestamp': data[-1]['timestamp']})

    total_profit = balance
    percentage_profit = (balance / data[0]['close'] - 1) * 100

    return {
        'total_profit': total_profit,
        'percentage_profit': percentage_profit,
        'trades': trades
    }
