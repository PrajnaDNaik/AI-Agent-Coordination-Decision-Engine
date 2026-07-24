class EmailTool:
    def send_email(self, recipient, subject, message):
        return (
            f"Email sent to {recipient}\n"
            f"Subject: {subject}\n"
            f"Message: {message}"
        )