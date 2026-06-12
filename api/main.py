# api/main.py

from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

from src.stock_analyst.crew import StockAnalystCrew

app = FastAPI(
    title="Stock Analyst API"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
class StockRequest(BaseModel):
    company: str
    ticker: str


@app.get("/")
def home():
    return {"message": "Welcome to the Stock Analyst API! Use the /analyze endpoint to get a report."}

@app.get("/health")
def health_check():
    return {"status": "ok"}




@app.post("/analyze")
def analyze_stock(request: StockRequest):

    try:
        result = (
            StockAnalystCrew()
            .crew()
            .kickoff(
                inputs={
                    "company": request.company,
                    "ticker": request.ticker
                }
            )
        )

        return {
            "success": True,
            "company": request.company,
            "ticker": request.ticker,
            "report": str(result)
        }

    except Exception as e:
        return {
            "success": False,
            "error": str(e)
        }
