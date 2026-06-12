import streamlit as st
from dotenv import load_dotenv
import sys, os

sys.path.insert(0, "src/stock_analyst")
load_dotenv()

from crew import StockAnalystCrew

# ── Page Config ──────────────────────────────────────────
st.set_page_config(
    page_title="Stock Analyst AI",
    page_icon="📈",
    layout="wide"
)

# ── Header ───────────────────────────────────────────────
st.title("📈 Stock Market Analysis — Multi-Agent AI")
st.caption("Powered by CrewAI · Groq · YFinance · Serper")
st.divider()

# ── Input Section ────────────────────────────────────────
col1, col2 = st.columns(2)
with col1:
    company = st.text_input("Company Name", placeholder="e.g. Apple")
with col2:
    ticker = st.text_input("Stock Ticker", placeholder="e.g. AAPL")

analyze_btn = st.button("🔍 Analyze Stock", type="primary", use_container_width=True)

# ── Run Crew ─────────────────────────────────────────────
if analyze_btn:
    if not company or not ticker:
        st.warning("Please enter both company name and ticker.")
    else:
        with st.spinner("🤖 Agents are researching, analyzing and writing your report..."):

            # Live agent status
            status = st.empty()
            status.info("📰 News Researcher agent working...")

            try:
                inputs = {"company": company, "ticker": ticker}
                result = StockAnalystCrew().crew().kickoff(inputs=inputs)

                status.success("✅ Analysis complete!")
                st.divider()

                # ── Output ───────────────────────────────
                st.subheader(f"📋 Investment Brief — {company} ({ticker.upper()})")
                st.markdown(str(result))

                # Download button
                st.download_button(
                    label="⬇️ Download Report",
                    data=str(result),
                    file_name=f"{ticker}_report.md",
                    mime="text/markdown"
                )

            except Exception as e:
                status.error(f"Error: {str(e)}")

# ── Footer ───────────────────────────────────────────────
st.divider()
st.caption("Built with CrewAI + Streamlit | For educational purposes only. Not financial advice.")