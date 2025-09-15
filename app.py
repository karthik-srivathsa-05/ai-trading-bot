from flask import Flask, render_template, request, redirect, url_for
from bot import analyze_stock, plot_stock

app = Flask(__name__)

#Portfolio dictionary with stock
portfolio = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    symbol = request.form['symbol'].upper()
    try:
        result = analyze_stock(symbol)
        chart = plot_stock(symbol)  

        return render_template(
            'stock_detail.html',
            symbol=symbol,
            signal=result["signal"],
            today_price=result["today_price"],
            predicted_price=result["predicted_price"],
            chart=chart
        )
    except Exception as e:
        return f"Error: {e}"

@app.route('/buy/<symbol>')
def buy_stock(symbol):
    portfolio[symbol] = "BUY"
    return redirect(url_for('show_portfolio'))

@app.route('/sell/<symbol>')
def sell_stock(symbol):
    portfolio[symbol] = "SELL"
    return redirect(url_for('show_portfolio'))

@app.route('/hold/<symbol>')
def hold_stock(symbol):
    portfolio[symbol] = "HOLD"
    return redirect(url_for('show_portfolio'))

@app.route('/portfolio')
def show_portfolio():
    charts = {}
    for stock in portfolio.keys():
        try:
            charts[stock] = plot_stock(stock)
        except Exception:
            charts[stock] = None
    return render_template('portfolio.html', portfolio=portfolio, charts=charts)

if __name__ == '__main__':
    app.run(debug=True)