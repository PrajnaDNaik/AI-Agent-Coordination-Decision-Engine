from agents.orchestrator import Orchestrator


class DecisionFlow:

    def __init__(self):
        self.orchestrator = Orchestrator()

    def process_request(self, query):

        result = self.orchestrator.run(
            query
        )

        return result
