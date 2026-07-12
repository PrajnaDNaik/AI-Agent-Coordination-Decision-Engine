from langchain_openai import ChatOpenAI

from prompts.templates import PLANNER_TEMPLATE
from config.settings import MODEL_NAME, TEMPERATURE


class PlannerAgent:

    def __init__(self):
        self.llm = ChatOpenAI(
            model=MODEL_NAME,
            temperature=TEMPERATURE
        )

    def create_plan(self, analysis):

        prompt = PLANNER_TEMPLATE.format(
            analysis=analysis
        )

        response = self.llm.invoke(prompt)

        return response.content