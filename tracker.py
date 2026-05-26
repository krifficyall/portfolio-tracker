import yfinance as yf
import pandas as pd


portfolio = {
    "AAPL": {"shares": 10, "avg_buy_price":150.00},
    "TSLA":{"shares": 5, "avg_buy_price": 200.00},
    "GOOGL":{"shares":3, "avg_buy_price":130.00}
}
data=[]
for symbol in portfolio:
    holding = portfolio[symbol]
    ticker = yf.Ticker(symbol)
    current_price = ticker.fast_info.last_price
    shares = holding["shares"]
    avg_buy = holding["avg_buy_price"]

    current_value = shares*current_price
    amount_invested=shares*avg_buy
    gain_loss = current_value-amount_invested   

    data.append({
        "Ticker":  symbol,
        "Shares":  shares,
        "Avg Buy Price": round(avg_buy, 2),
        "current_Price": round(current_price, 2)
        "current_value": round(current_value, 2)
        "Gain/Loss {$}": round(gain_loss, 2)
    })