from dotenv import load_dotenv
from crew import StockAnalystCrew

load_dotenv()

def run(company: str, ticker: str):
    inputs = {
        "company": company,
        "ticker": ticker
    }
    result = StockAnalystCrew().crew().kickoff(inputs=inputs)
    return result

if __name__ == "__main__":
    print(run("Apple", "AAPL"))