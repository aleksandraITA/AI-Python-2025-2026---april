class Employee: 
    EUR_TO_RSD = 117.5
    COMPANY_NAME = "ABC"

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def convertSalaryToEUR(self):
        return self.salary / Employee.EUR_TO_RSD
    
    @staticmethod
    def convertEURtoRSD(eurAmount):
        return eurAmount * Employee.EUR_TO_RSD
            
    def display_info(self):
        print(f"[{Employee.COMPANY_NAME}] {self.name}, {self.position} - {self.salary}")       
    
    def __str__(self):
        return f"[Employee]: {self.name}, {self.position} - {self.salary}"
 
# napravite static metodu isValidSalary koja proverava da li je plata > 0 i vraca True/False    
    @staticmethod
    def isValidSalary(salary):
        return salary > 0     
     
res = Employee.convertEURtoRSD(1000)
print(res)

print(Employee.isValidSalary(150))
print(Employee.isValidSalary(-1520))

### Hello from Nedim!