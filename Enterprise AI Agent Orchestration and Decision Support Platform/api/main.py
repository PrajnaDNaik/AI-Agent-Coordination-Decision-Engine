from fastapi import FastAPI
from pydantic import BaseModel

from workflows.decision_flow import DecisionFlow

app = FastAPI(
    title="Enterprise AI Agent Orchestration Platform"
)

workflow = DecisionFlow()


class BusinessRequest(BaseModel):
    query: str


@app.get("/")
def home():

    return {
        "message":
        "Enterprise AI Agent Orchestration Platform Running"
    }


@app.post("/decision-support")
def decision_support(request: BusinessRequest):

    result = workflow.process_request(
        request.query
    )

    return result