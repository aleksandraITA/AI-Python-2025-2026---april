from employee import Employee

class Intern(Employee):
    def __init__(self, name, email, project_assigned):
        super().__init__(name, email)
        self.project_assigned = project_assigned

    def work_on_project(self):
        print(f"{self.name} is working on a project {self.project_assigned}")