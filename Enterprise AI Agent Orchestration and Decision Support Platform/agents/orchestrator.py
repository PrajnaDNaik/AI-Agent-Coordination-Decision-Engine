from langchain_google_genai import ChatGoogleGenerativeAI

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

        self.decision_llm = ChatGoogleGenerativeAI(
            model=MODEL_NAME,
            temperature=TEMPERATURE
        )

    def run(self, query):

        
        analysis = self.analyst.analyze(query)

        
        plan = self.planner.create_plan(analysis)

    
        execution = self.executor.execute(plan)

        
        decision_prompt = DECISION_TEMPLATE.format(
            analysis=analysis,
            plan=plan,
            execution=execution
        )

        response = self.decision_llm.invoke(decision_prompt)

        if hasattr(response, "content"):
            if isinstance(response.content, list):
                final_decision = "".join(
                    part["text"] if isinstance(part, dict) else str(part)
                    for part in response.content
                )
            else:
                final_decision = response.content
        else:
            final_decision = str(response)

        return {
            "analysis": analysis,
            "plan": plan,
            "execution": execution,
            "decision": final_decision
        }


if __name__ == "__main__":

    orchestrator = Orchestrator()

    query = input("Enter your enterprise query: ")

    result = orchestrator.run(query)

    print("\n===== ANALYSIS =====")
    print(result["analysis"])

    print("\n===== PLAN =====")
    print(result["plan"])

    print("\n===== EXECUTION =====")
    print(result["execution"])

    print("\n===== FINAL DECISION =====")
    print(result["decision"])
