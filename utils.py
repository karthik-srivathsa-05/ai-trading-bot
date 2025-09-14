import numpy as np
import pandas as pd

def calculate_moving_average(data, window=5):
    """Calculates the simple moving average."""
    return data['Close'].rolling(window=window).mean()

def calculate_volatility(data, window=5):
    """Calculates the rolling standard deviation (volatility)."""
    return data['Close'].rolling(window=window).std()

def calculate_rsi(data, window=14):
    """Calculates the Relative Strength Index (RSI)."""
    delta = data['Close'].diff()
    gain = (delta.where(delta > 0, 0)).ewm(alpha=1/window, adjust=False).mean()
    loss = (-delta.where(delta < 0, 0)).ewm(alpha=1/window, adjust=False).mean()
    
    # Avoid division by zero
    rs = gain / loss
    rs = rs.replace([np.inf, -np.inf], np.nan).fillna(0)
    
    rsi = 100 - (100 / (1 + rs))
    return rsi