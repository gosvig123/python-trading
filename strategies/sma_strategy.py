# Filename: sma_strategy.py

from indicators.sma import calculate_moving_average

def simple_ma_strategy(data):
    """
    Simple moving average crossover strategy that can handle any size of data.

    Parameters:
    - data: A list of dictionaries with 'close' prices.

    Returns:
    - A trading signal ('buy', 'sell', or 'hold').
    """
    # Calculate moving averages without assuming minimum data size
    short_ma = calculate_moving_average(data, 20)
    long_ma = calculate_moving_average(data, 30)

    # Ensure we have at least one element in both moving averages to compare
    if len(short_ma) > 1 and len(long_ma) > 1 and short_ma[-1] is not None and long_ma[-1] is not None:
        if short_ma[-2] < long_ma[-2] and short_ma[-1] > long_ma[-1]:
            return 'buy'
        elif short_ma[-2] > long_ma[-2] and short_ma[-1] < long_ma[-1]:
            return 'sell'

    # Default to 'hold' if not enough data to decide or no crossover detected
    return 'hold'
