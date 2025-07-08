import streamlit as st
import yfinance as yf
import ta
from stock_analysis import analyze_stock
from ai_advisor import get_advice
from news_fetcher import get_stock_news

# Initialize watchlist in session state 
if "watchlist" not in st.session_state:
    st.session_state.watchlist = []

st.title("📈 Stock Data")

#  tabs
tabs = st.tabs(["Search", "Watchlist", "News"])

with tabs[0]:
    st.header("Stock Search")

    ticker_input = st.text_input("Enter a stock ticker:", value="AAPL")

    if ticker_input:
        try:
            ticker = yf.Ticker(ticker_input)
            df = ticker.history(period="max")

            if df.empty:
                st.error("No data found.")
            else:
                # Technical indicators
                df["macd"] = ta.trend.macd(df["Close"])
                df["sma_20"] = ta.trend.sma_indicator(df["Close"], window=20)
                df["rsi"] = ta.momentum.rsi(df["Close"])

                analysis = analyze_stock(df)

                st.subheader(f"{ticker_input} Price Chart")
                st.line_chart(df["Close"])

                # WATCHLIST BUTTON
                if st.button("➕ Add to Watchlist"):
                    if ticker_input not in st.session_state.watchlist:
                        st.session_state.watchlist.append(ticker_input)
                        st.success(f"{ticker_input} added to your watchlist!")
                    else:
                        st.info(f"{ticker_input} is already in your watchlist.")

                st.subheader("Indicators")
                st.metric("Close", f"${analysis['close']:.2f}")
                st.metric("MACD", f"{analysis['macd']:.2f}")
                st.metric("SMA 20", f"{analysis['sma_20']:.2f}")
                st.metric("RSI", f"{analysis['rsi']:.2f}")
                st.metric("Signal", analysis["advice"].upper())

                st.subheader("AI Advice")
                advice = get_advice(ticker_input, analysis)
                st.write(advice)

                

        except Exception as e:
            st.error(f"Error: No stock found")


with tabs[1]:
    st.header("Your Watchlist")

    if not st.session_state.watchlist:
        st.info("Your watchlist is empty. Add stocks from the Search tab.")
    else:
        for symbol in st.session_state.watchlist:
            st.write(f"### {symbol}")
            try:
                ticker = yf.Ticker(symbol)
                df = ticker.history(period="max")

                if df.empty:
                    st.write("No data available.")
                else:
                    st.line_chart(df["Close"])

                price = ticker.info.get("currentPrice", "N/A")
                st.write(f"Current Price: ${price}")
            except Exception as e:
                st.write(f"Error loading {symbol}: {e}")


with tabs[2]:
    st.header("📰 Stock Market News")
    news_ticker = st.text_input("Enter stock ticker to get recent news:", value="AAPL")

    if news_ticker:
        news_items = get_stock_news(news_ticker)                                                                                                                                                                                                                                                   
        if not news_items:
            st.warning("No news found or API issue.")
        else:
            for article in news_items:
                st.subheader(article["title"])
                st.write(f"Source: {article['source']}")
                st.write(f"Published: {article['publishedAt']}")
                st.markdown(f"[Read more]({article['url']})")
                st.markdown("---")

