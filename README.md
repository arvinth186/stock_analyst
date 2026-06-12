# 📈 Stock Analyst AI

A Multi-Agent AI-powered stock analysis platform built using **CrewAI**, **FastAPI**, **Groq LLM**, **YFinance**, and **Serper Search**.

The system uses multiple specialized AI agents to research financial news, analyze stock fundamentals, assess investment risks, and generate a comprehensive investment brief for any publicly traded company.

---

## 🚀 Features

* Multi-Agent Financial Analysis
* Latest News & Market Sentiment Research
* Real-Time Stock Data using YFinance
* Risk Assessment Engine
* AI Generated Investment Reports
* FastAPI Backend API
* Streamlit Frontend
* Swagger API Documentation
* Downloadable Investment Reports
* Deployable on Render

---

## 🏗️ Architecture

```text
User
 │
 ▼
Streamlit UI
 │
 ▼
FastAPI API
 │
 ▼
CrewAI Multi-Agent System
 │
 ├── News Researcher Agent
 ├── Financial Analyst Agent
 ├── Risk Assessment Agent
 └── Report Writer Agent
 │
 ▼
Final Investment Report
```

---

## 🤖 Agents

### News Researcher

Responsible for:

* Searching latest company news
* Market sentiment analysis
* Earnings reports
* Analyst opinions

### Financial Analyst

Responsible for:

* Current stock price
* PE ratio
* Market capitalization
* Volume analysis
* 52-week high/low
* Price trend analysis

### Risk Assessment Specialist

Responsible for:

* Market risks
* Company-specific risks
* Technical risks
* Macro-economic risks

### Report Writer

Responsible for:

* Executive summary
* Financial snapshot
* News highlights
* Risk assessment
* Final recommendation

---

## 📂 Project Structure

```text
stock_analyst/
│
├── api/
│   └── main.py
│
├── src/
│   └── stock_analyst/
│       ├── config/
│       │   ├── agents.yaml
│       │   └── tasks.yaml
│       │
│       ├── tools/
│       │   ├── search_tool.py
│       │   └── yfinance_tool.py
│       │
│       └── crew.py
│
├── app.py
├── requirements.txt
├── pyproject.toml
├── README.md
└── .gitignore
```

---

## 🛠️ Tech Stack

### Backend

* FastAPI
* CrewAI
* Python

### AI & LLM

* Groq
* Llama Models

### Data Sources

* YFinance
* Serper Search API

### Frontend

* Streamlit

### Deployment

* Render

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/arvinth186/stock_analyst.git

cd stock_analyst
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
SERPER_API_KEY=your_serper_api_key
```

---

## ▶️ Run FastAPI Backend

```bash
uvicorn api.main:app --reload
```

API Docs:

```text
http://localhost:8000/docs
```

---

## ▶️ Run Streamlit Frontend

```bash
streamlit run app.py
```

Frontend:

```text
http://localhost:8501
```

---

## 📡 API Endpoint

### Analyze Stock

**POST**

```text
/api/analyze
```

Request:

```json
{
  "company": "Apple",
  "ticker": "AAPL"
}
```

Response:

```json
{
  "success": true,
  "company": "Apple",
  "ticker": "AAPL",
  "report": "Generated Investment Report..."
}
```

---

## 📄 Sample Report Sections

The generated investment brief contains:

* Executive Summary
* Financial Snapshot
* News & Sentiment
* Risk Assessment
* Investment Recommendation

---

## 🌐 Deployment

This project is designed for deployment on Render.

Build Command:

```bash
pip install -r requirements.txt
```

Start Command:

```bash
uvicorn api.main:app --host 0.0.0.0 --port $PORT
```

---

## ⚠️ Disclaimer

This project is intended for educational and research purposes only.

The generated reports do not constitute financial advice. Always conduct your own research before making investment decisions.

---

## 👨‍💻 Author

Arvinth

GitHub:
https://github.com/arvinth186
