from crewai import Agent, Task, Crew, Process
from crewai.project import CrewBase, agent, task, crew
from src.stock_analyst.tools.search_tool import search_tool
from src.stock_analyst.tools.yfinance_tool import get_stock_data

@CrewBase
class StockAnalystCrew:

    agents_config = "config/agents.yaml"
    tasks_config = "config/tasks.yaml"

    # ── Agents ──────────────────────────────────────────
    @agent
    def news_researcher(self) -> Agent:
        return Agent(
            config=self.agents_config["news_researcher"],
            tools=[search_tool]
        )

    @agent
    def financial_analyst(self) -> Agent:
        return Agent(
            config=self.agents_config["financial_analyst"],
            tools=[get_stock_data]
        )

    @agent
    def risk_assessor(self) -> Agent:
        return Agent(
            config=self.agents_config["risk_assessor"],
            tools=[search_tool]
        )

    @agent
    def report_writer(self) -> Agent:
        return Agent(
            config=self.agents_config["report_writer"],
            tools=[]
        )

    # ── Tasks ────────────────────────────────────────────
    @task
    def research_news_task(self) -> Task:
        return Task(config=self.tasks_config["research_news_task"])

    @task
    def analyze_financials_task(self) -> Task:
        return Task(config=self.tasks_config["analyze_financials_task"])

    @task
    def assess_risk_task(self) -> Task:
        return Task(config=self.tasks_config["assess_risk_task"])

    @task
    def generate_report_task(self) -> Task:
        return Task(
            config=self.tasks_config["generate_report_task"],
            output_file="report.md"   # saves final report to file
        )

    # ── Crew ─────────────────────────────────────────────
    @crew
    def crew(self) -> Crew:
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True
        )