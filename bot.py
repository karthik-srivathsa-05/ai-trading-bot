import yfinance as yf
import matplotlib.pyplot as plt
import os

def analyze_stock(symbol):
    data = yf.download(symbol, period="6mo", interval="1d")
    if data.empty:
        raise ValueError("No data found for this symbol")

    # calculate moving averages
    data['SMA20'] = data['Close'].rolling(window=20).mean()
    data['SMA50'] = data['Close'].rolling(window=50).mean()

    if data['SMA20'].iloc[-1] > data['SMA50'].iloc[-1]:
        return "BUY"
    elif data['SMA20'].iloc[-1] < data['SMA50'].iloc[-1]:
        return "SELL"
    else:
        return "HOLD"

def plot_stock(symbol):
    data = yf.download(symbol, period="6mo", interval="1d")
    if data.empty:
        raise ValueError("No data found for this symbol")

    # recalculate here too
    data['SMA20'] = data['Close'].rolling(window=20).mean()
    data['SMA50'] = data['Close'].rolling(window=50).mean()

    plt.figure(figsize=(8,4))
    plt.plot(data.index, data['Close'], label="Close Price", color="blue")
    plt.plot(data.index, data['SMA20'], label="SMA20", color="green")
    plt.plot(data.index, data['SMA50'], label="SMA50", color="red")
    plt.legend()
    plt.title(f"{symbol} Stock Analysis")

    chart_path = f"static/charts/{symbol}.png"
    plt.savefig(chart_path)
    plt.close()
    return chart_path