# Filename: backtest_strategy.py

def run_backtest(strategy, data, initial_balance=10000):
    """
    Run a backtest of a trading strategy on historical data.

    Parameters:
    - strategy: A function that takes historical data and returns a trading signal ('buy', 'sell', 'hold').
    - data: A list of dictionaries with 'timestamp' and 'close' prices.
    - initial_balance: Initial balance to start the backtest with (default 10000).

    Returns:
    - A dictionary with total profit, percentage profit, and a list of trades.
    """
    balance = initial_balance
    holding = False
    total_profit = 0
    
    trades = []

    for i in range(1, len(data)):
        signal = strategy(data[:i])
        price = data[i]['close']
        
        if signal == 'buy' and not holding:
            balance -= price
            holding = True
            trades.append({'timestamp': data[i]['timestamp'], 'action': 'buy', 'price': price, 'balance': balance})
        
        elif signal == 'sell' and holding:
            balance += price
            total_profit += price - trades[-1]['price']  # Calculate profit from the last buy
            holding = False
            trades.append({'timestamp': data[i]['timestamp'], 'action': 'sell', 'price': price, 'balance': balance})
        
        elif signal == 'hold':
            trades.append({'timestamp': data[i]['timestamp'], 'action': 'hold', 'price': price, 'balance': balance})
        
        else:
            raise ValueError('Invalid strategy')

    # Calculate final metrics
    final_balance = balance + (data[-1]['close'] if holding else 0)  # Add the value of holdings to final balance
    total_profit = final_balance - initial_balance
    percentage_profit = (total_profit / initial_balance) * 100

    return {
        'initial_balance': initial_balance,
        'final_balance': final_balance,
        'total_profit': total_profit,
        'percentage_profit': percentage_profit,
        'trades': trades
    }
