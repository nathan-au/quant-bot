import yfinance as yf
import matplotlib.pyplot as plt
from google import genai
from dotenv import load_dotenv
import os

# Load .env file
load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=gemini_api_key)

# Define the ticker symbol and get data
ticker_symbol = "AAPL"
period = "5d"
ticker = yf.Ticker(ticker_symbol)
historical_data = ticker.history(period=period).dropna(subset=["Close"])
financials = ticker.financials

# Print data
print("\nPrice data for", ticker_symbol, "over", period)
print(historical_data)
print("\nFinancials:")
print(financials)

# Plot closing price
plt.figure(figsize=(14, 7))
plt.plot(historical_data.index, historical_data["Close"], label="Close Price", color="blue", linewidth=2)
plt.title(f"{ticker_symbol} Closing Price - Last {period}")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()

# Prepare data for Gemini
historical_str = historical_data.to_string()
financials_str = financials.to_string()

prompt = f"""
Based on the following price data and financials, should I buy, sell, or hold {ticker_symbol}?

Price data (last {period}):
{historical_str}

Financials:
{financials_str}

Respond with
"""

# Send to Gemini
gemini_response = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt
)

print("\nGemini's recommendation:")
print(gemini_response.text)