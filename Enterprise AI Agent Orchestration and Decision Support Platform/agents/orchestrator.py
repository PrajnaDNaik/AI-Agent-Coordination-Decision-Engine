
from langchain_openai import ChatOpenAI

from agents.analyst_agent import AnalystAgent
from agents.planner_agent import PlannerAgent
from agents.execution_agent import ExecutionAgent

from prompts.templates import DECISION_TEMPLATE
from config.settings import MODEL_NAME, TEMPERATURE


class Orchestrator:

    def __init__(self):

        self.analyst = AnalystAgent()
        self.planner = PlannerAgent()
        self.executor = ExecutionAgent()

        self.decision_llm = ChatOpenAI(
            model=MODEL_NAME,
            temperature=TEMPERATURE
        )

    def run(self, query):

        analysis = self.analyst.analyze(query)

        plan = self.planner.create_plan(
            analysis
        )

        execution = self.executor.execute(
            plan
        )

        decision_prompt = DECISION_TEMPLATE.format(
            analysis=analysis,
            plan=plan,
            execution=execution
        )

        final_decision = self.decision_llm.invoke(
            decision_prompt
        ).content

        return {
            "analysis": analysis,
            "plan": plan,
            "execution": execution,
            "decision": final_decision
        