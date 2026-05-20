from fastapi import FastAPI
from pydantic import BaseModel

from agents.planner import PlannerAgent
from agents.sql_agent import SQLAgent
from agents.chart_agent import ChartAgent
from agents.insight_agent import InsightAgent
from agents.memory_agent import MemoryAgent

from core.database import load_csv

app = FastAPI()

planner = PlannerAgent()
sql_agent = SQLAgent()
chart_agent = ChartAgent()
insight_agent = InsightAgent()
memory_agent = MemoryAgent()

load_csv("data/sales.csv", "sales")

SCHEMA = '''
Table: sales

Columns:
- date
- region
- product
- revenue
- quantity
'''


class QueryRequest(BaseModel):
    question: str


@app.get("/")
def home():
    return {
        "message": "AI Data Analysis Agent Running"
    }


@app.post("/analyze")
def analyze(request: QueryRequest):

    try:

        plan = planner.run(request.question)

        sql = sql_agent.generate_sql(
            request.question,
            SCHEMA
        )

        result_df = sql_agent.execute(sql)

        insight = insight_agent.analyze(
            request.question,
            result_df.to_string()
        )

        memory_agent.save(
            request.question,
            insight
        )

        return {
            "success": True,
            "plan": plan,
            "sql": sql,
            "data": result_df.to_dict(),
            "insight": insight
        }

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }
