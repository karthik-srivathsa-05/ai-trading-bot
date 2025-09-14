from flask import Flask, render_template, request, redirect, url_for
from bot import analyze_stock, plot_stock
import os
import random

@app.context_processor
def inject_random():
    # Makes a random() function available inside Jinja templates
    return dict(random=lambda: random.randint(0, 100000))

app = Flask(__name__)

# simple portfolio in memory
portfolio = []

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    symbol = request.form['symbol'].upper()
    try:
        signal = analyze_stock(symbol)
        chart_path = plot_stock(symbol)
        return render_template('index.html', result=signal, chart=chart_path)
    except Exception as e:
        return render_template('index.html', result=f"Error: {e}", chart=None)

@app.route('/portfolio')
def show_portfolio():
    return render_template('portfolio.html', portfolio=portfolio)

@app.route('/add_stock', methods=['POST'])
def add_stock():
    symbol = request.form['symbol'].upper()
    if symbol not in portfolio:
        portfolio.append(symbol)
    return redirect(url_for('show_portfolio'))

@app.route('/stock/<symbol>')
def stock_detail(symbol):
    try:
        signal = analyze_stock(symbol)
        chart_path = plot_stock(symbol)
        return render_template('stock_detail.html', symbol=symbol, signal=signal, chart=chart_path)
    except Exception as e:
        return render_template('stock_detail.html', symbol=symbol, signal=f"Error: {e}", chart=None)

if __name__ == '__main__':
    os.makedirs("static/charts", exist_ok=True)
    app.run(debug=True)