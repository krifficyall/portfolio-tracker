import yfinance as yf
import pandas as pd
import streamlit as st

#PAGE SETUP YALL

st.set_page_config(page_title="Portfolio Tracker", layout="wide")
st.title("📈 My Portfolio Tracker")
st.caption("Prices update every time you'll refresh this page.")

#your holdings 

portfolio = {
    "AAPL": {"shares": 10, "avg_buy_price": 150.00},
    "TSLA": {"shares": 5, "avg_buy_price": 200.00},
    "GOOGL": {"shares": 3, "avg_buy_price": 130.00},
}
st.subheader("Fetching live prices...")
data = []
for symbol in portfolio:
    holding = portfolio[symbol]
    ticker = yf.Ticker(symbol)
    current_price = ticker.fast_info.last_price

    shares        = holding["shares"]
    avg_buy       = holding["avg_buy_price"]
    current_value = shares * current_price
    amount_invested = shares * avg_buy
    gain_loss     = current_value - amount_invested
    gain_loss_pct = (gain_loss / amount_invested) * 100

    data.append({
        "Ticker":         symbol,
        "Shares":         shares,
        "Avg Buy ($)":    round(avg_buy, 2),
        "Current ($)":    round(current_price, 2),
        "Value ($)":      round(current_value, 2),
        "Gain/Loss ($)":  round(gain_loss, 2),
        "Gain/Loss (%)":  round(gain_loss_pct, 2),
    })

df = pd.DataFrame(data)

total_value = df["Value ($)"].sum()
total_invested = 0

for s in portfolio:
    amount = portfolio[s]["shares"] * portfolio[s]["avg_buy_price"]
    total_invested = total_invested + amount

total_gain = total_value - total_invested

col1, col2, col3 = st.coulumns(3)
col1.metric("Total Value",     f"${total_value:.2f}")
col2.metric("Total Invested",  f"${total_invested:.2f}")
col3.metric("Total Gain/Loss", f"${total_gain:.2f}",
            delta=f"${total_gain:.2f}")   

st.subheader("Your Holdings")
st.dataframe(df, use_container_width=True)

# ── CHART ────────────────────────────────────────────
st.subheader("Portfolio Breakdown")
st.bar_chart(df.set_index("Ticker")["Value ($)"])   