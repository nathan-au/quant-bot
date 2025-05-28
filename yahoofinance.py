import yfinance as yf
import matplotlib.pyplot as plt

# Define the ticker symbol
ticker_symbol = "AAPL"
ticker = yf.Ticker(ticker_symbol)
period = "5d"

historical_data = ticker.history(period)
print()
print("Price data for " + ticker_symbol + " over " + period)
print(historical_data)

# financials = ticker.financials
# print("\nFinancials:")
# print(financials)

# Step 2: Plot just the closing price
plt.figure(figsize=(14, 7))  # Good balance for most stock/crypto charts
plt.plot(historical_data.index, historical_data["Close"], label="Close Price", color="blue", linewidth=2)

# Formatting
plt.title(f"{ticker_symbol} Closing Price - Last {period}")
plt.xlabel("Date")
plt.ylabel("Price (USD)")
plt.legend()
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()