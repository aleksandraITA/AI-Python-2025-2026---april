class SalesManager:
    def __init__(self, name, email, sales_target):
        self.name = name
        self.email = email
        self.sales_target = sales_target    
           
    def send_email(self, subject, message):
            print(f"Sending email to {self.email} with subject '{subject}' and message '{message}'")

    def track_sales(self):
        print(f"{self.name} has the sales target: {self.sales_target}")