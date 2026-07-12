from langchain_openai import ChatOpenAI

from prompts.templates import EXECUTION_TEMPLATE
from config.settings import MODEL_NAME, TEMPERATURE


class ExecutionAgent:

    def __init__(self):
        self.llm = ChatOpenAI(
            model=MODEL_NAME,
            temperature=TEMPERATURE
        )

    def execute(self, plan):

        prompt = EXECUTION_TEMPLATE.format(
            plan=plan
        )

        response = self.llm.invoke(prompt)

        return response.content