import yfinance as yf

ticker = yf.Ticker("AAPL")
df = ticker.history(period="6mo", interval="1d")

print("Shape:", df.shape)
print(df.head())
