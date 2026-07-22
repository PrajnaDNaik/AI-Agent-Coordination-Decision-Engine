from langchain_google_genai import ChatGoogleGenerativeAI

from prompts.templates import EXECUTION_TEMPLATE
from config.settings import MODEL_NAME, TEMPERATURE


class ExecutionAgent:

    def __init__(self):
        self.llm = ChatGoogleGenerativeAI(
            model=MODEL_NAME,
            temperature=TEMPERATURE
        )

    def execute(self, plan):

        prompt = EXECUTION_TEMPLATE.format(
            plan=plan
        )

        response = self.llm.invoke(prompt)

        if hasattr(response, "content"):
            if isinstance(response.content, list):
                return "".join(
                    part["text"] if isinstance(part, dict) else str(part)
                    for part in response.content
                )
            return response.content

        return str(response)
