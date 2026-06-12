import yfinance as yf
from crewai.tools import tool

@tool("Stock Data Fetcher")
def get_stock_data(ticker: str) -> str:
    """Fetches current stock price, PE ratio, market cap,
    52-week high/low, and volume for a given ticker symbol."""
    try:
        stock = yf.Ticker(ticker)
        info = stock.info
        hist = stock.history(period="30d")

        data = {
            "Current Price": info.get("currentPrice", "N/A"),
            "52W High": info.get("fiftyTwoWeekHigh", "N/A"),
            "52W Low": info.get("fiftyTwoWeekLow", "N/A"),
            "PE Ratio": info.get("trailingPE", "N/A"),
            "Market Cap": info.get("marketCap", "N/A"),
            "Volume": info.get("volume", "N/A"),
            "30D Price Change": f"{((hist['Close'].iloc[-1] - hist['Close'].iloc[0]) / hist['Close'].iloc[0] * 100):.2f}%"
        }

        return "\n".join([f"{k}: {v}" for k, v in data.items()])
    except Exception as e:
        return f"Error fetching data: {str(e)}"