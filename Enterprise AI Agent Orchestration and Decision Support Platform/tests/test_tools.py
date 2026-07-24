from tools.crm_tool import CRMTool
from tools.database_tool import DatabaseTool
from tools.email_tool import EmailTool
from tools.api_connector import APIConnector


def test_tools():
    crm = CRMTool()
    db = DatabaseTool()
    email = EmailTool()
    api = APIConnector()

    print("===== CRM TOOL =====")
    print(crm.get_customer_info("ABC Corporation"))

    print("\n===== DATABASE TOOL =====")
    print(db.fetch_data("Customer Records"))

    print("\n===== EMAIL TOOL =====")
    print(email.send_email(
        "manager@company.com",
        "Test Email",
        "This is a test."
    ))

    print("\n===== API TOOL =====")
    print(api.fetch_api_data("https://jsonplaceholder.typicode.com/todos/1"))


if __name__ == "__main__":
    test_tools()