from langchain_google_genai import ChatGoogleGenerativeAI

from prompts.templates import ANALYST_TEMPLATE
from config.settings import MODEL_NAME, TEMPERATURE


class AnalystAgent:

    def __init__(self):
        print("Using model:", MODEL_NAME)   

        self.llm = ChatGoogleGenerativeAI(
            model=MODEL_NAME,
            temperature=TEMPERATURE
        )

    def analyze(self, query):

        prompt = ANALYST_TEMPLATE.format(
            query=query
        )

        response = self.llm.invoke(prompt)

        return response.text()
