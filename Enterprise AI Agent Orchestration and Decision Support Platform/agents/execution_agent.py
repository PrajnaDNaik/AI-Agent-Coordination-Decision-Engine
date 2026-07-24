from tools.crm_tool import CRMTool
from tools.database_tool import DatabaseTool
from tools.email_tool import EmailTool
from tools.api_connector import APIConnector


class ExecutionAgent:
    def __init__(self):
        self.crm = CRMTool()
        self.database = DatabaseTool()
        self.email = EmailTool()
        self.api = APIConnector()

    def execute(self, task):
        task = task.lower()

        try:
            if "customer" in task:
                return self.crm.get_customer_info("ABC Corporation")

            elif "database" in task or "data" in task:
                return self.database.fetch_data(task)

            elif "email" in task:
                return self.email.send_email(
                    "manager@company.com",
                    "Enterprise Update",
                    "Workflow executed successfully."
                )

            elif "api" in task:
                return self.api.fetch_api_data(
                    "https://jsonplaceholder.typicode.com/todos/1"
                )

            else:
                return "No suitable enterprise tool found. General task executed."

        except Exception as e:
            return f"Execution Error: {e}"