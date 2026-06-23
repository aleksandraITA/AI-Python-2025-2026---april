class Employee:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def send_email(self, subject, message):
        print(f"Sending email to {self.email} with subject '{subject}' and message '{message}'")
