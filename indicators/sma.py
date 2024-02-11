def calculate_moving_average(data, window):
    """
    Calculate the simple moving average (SMA) without None placeholders for the given data.

    Parameters:
    - data (list): A list of dictionaries with keys 'timestamp', 'open', 'high', 'low', 'close'.
    - window (int): The number of periods over which to calculate the SMA.

    Returns:
    - list: A list containing the SMA values starting from the point where the first SMA can be calculated.
    """
    if not data or window <= 0:
        return []

    moving_averages = []
    closing_prices = [item['close'] for item in data]

    for i in range(window - 1, len(closing_prices)):
        window_slice = closing_prices[i - window + 1:i + 1]
        moving_averages.append(sum(window_slice) / window)

    return moving_averages

