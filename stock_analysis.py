import pandas as pd
import ta  # technical analysis library

def analyze_stock(df):
    # Check if there's any data to work with
    if df.empty or len(df) < 2:
        return {"error": "Not enough stock data to analyze. Try a different ticker or date range."}

    # Add technical indicators (like moving averages, RSI, etc.)
    df = ta.add_all_ta_features(
        df,
        open="Open",
        high="High",
        low="Low",
        close="Close",
        volume="Volume"
    )

    # You can add more logic here to give advice
    latest_close = df["Close"].iloc[-1]
    rsi = df["momentum_rsi"].iloc[-1]  # RSI = Relative Strength Index
    df["macd"] = ta.trend.macd(df["Close"])
    df['sma_20'] = ta.trend.sma_indicator(df['Close'], window=20)

    # Simple advice based on RSI
    if rsi > 70:
        advice = "This stock might be overbought. Be cautious."
    elif rsi < 30:
        advice = "This stock might be oversold. Could be a buying opportunity."
    else:
        advice = "This stock is trading normally."

    return {
        "message": "Analysis complete.",
        "latest_price": latest_close,
        "rsi": rsi,
        "advice": advice,
        "df": df,
        "macd": df["macd"].iloc[-1],
        "close": df["Close"].iloc[-1],
        "sma_20": df["sma_20"].iloc[-1],
    }
