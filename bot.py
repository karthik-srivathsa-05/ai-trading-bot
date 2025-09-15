import yfinance as yf
import matplotlib.pyplot as plt
import numpy as np
import os

def analyze_stock(symbol):
    data = yf.download(symbol, period="6mo", interval="1d")
    if data.empty:
        raise ValueError("No data found for this symbol")

    data['SMA20'] = data['Close'].rolling(window=20).mean()
    data['SMA50'] = data['Close'].rolling(window=50).mean()

    today_price = float(data['Close'].iloc[-1])

    #simple trend-based prediction using linear regression
    x = np.arange(len(data['Close']))
    y = data['Close'].values
    coeffs = np.polyfit(x, y, deg=1)
    predicted = np.polyval(coeffs, x[-1] + 1)
    predicted_price = float(predicted)

    if data['SMA20'].iloc[-1] > data['SMA50'].iloc[-1]:
        signal = "BUY"
    elif data['SMA20'].iloc[-1] < data['SMA50'].iloc[-1]:
        signal = "SELL"
    else:
        signal = "HOLD"

    return {
        "signal": signal,
        "today_price": round(today_price, 2),
        "predicted_price": round(predicted_price, 2)
    }

def plot_stock(symbol):
    data = yf.download(symbol, period="6mo", interval="1d")
    if data.empty:
        raise ValueError("No data found for this symbol")

    data['SMA20'] = data['Close'].rolling(window=20).mean()
    data['SMA50'] = data['Close'].rolling(window=50).mean()

    plt.figure(figsize=(8, 4))
    plt.plot(data.index, data['Close'], label="Close Price", color="blue")
    plt.plot(data.index, data['SMA20'], label="SMA20", color="green")
    plt.plot(data.index, data['SMA50'], label="SMA50", color="red")
    plt.legend()
    plt.title(f"{symbol} Stock Analysis")

    os.makedirs("static/charts", exist_ok=True)
    chart_path = f"charts/{symbol}.png"
    plt.savefig(f"static/{chart_path}")
    plt.close()
    return chart_path