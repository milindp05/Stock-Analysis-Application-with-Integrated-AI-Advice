from openai import OpenAI


client = OpenAI() 

def get_advice(ticker, analysis):
    prompt = (
        f"Analyze the following stock data for {ticker}:\n"
        f"Close Price: {analysis['close']:.2f}\n"
        f"SMA 20: {analysis['sma_20']:.2f}\n"
        f"RSI: {analysis['rsi']:.2f}\n"
        f"MACD: {analysis['macd']:.4f}\n"
        f"Signal: {analysis['advice']}\n\n"
        "Please provide a detailed, professional trading advice based on this data."
    )

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are an expert financial advisor."},
            {"role": "user", "content": prompt}
        ]
    )
    return response.choices[0].message.content
