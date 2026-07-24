class CRMTool:
    def get_customer_info(self, customer_name):
        return {
            "customer": customer_name,
            "status": "Active",
            "subscription": "Premium",
            "last_interaction": "2 days ago"
        }

    def create_customer(self, customer_name):
        return f"Customer '{customer_name}' created successfully."