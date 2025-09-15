## Trading Bot

A simple Flask-based Stock Trading Simulator that lets users analyze stocks, view BUY/SELL/HOLD signals, and simulate trades in a portfolio.

## Features

1. Stock Search & Analysis – Enter a ticker symbol (e.g., AAPL, TSLA).

2. Signals – Basic rule-based signals (BUY/SELL/HOLD) using moving averages.

3. Portfolio Simulation – Simulate Buy, Sell, or Hold decisions.

## Tech Stack

1. Backend: Python, Flask

2. Frontend: HTML, Jinja2, CSS

3. Data: Yahoo Finance (yfinance)

4. Visualization: Matplotlib

## Installation & Usage

1. Clone the repository

git clone https://github.com/karthik-srivathsa-05/ai-trading-bot.git
cd ai-trading-bot

2. Create virtual environment & install dependencies
 
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows

pip install -r requirements.txt

3. Run the Flask server
python app.py

4. Open in browser