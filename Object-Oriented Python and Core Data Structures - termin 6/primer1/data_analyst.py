class DataAnalyst:
    def __init__(self, name, email, analysis_tool):
        self.name = name
        self.email = email
        self.analysis_tool = analysis_tool
        
    def send_email(self, subject, message):
            print(f"Sending email to {self.email} with subject '{subject}' and message '{message}'")
      
    def analyze_data(self):
        print(f"{self.name} is analysing data using {self.analysis_tool}")