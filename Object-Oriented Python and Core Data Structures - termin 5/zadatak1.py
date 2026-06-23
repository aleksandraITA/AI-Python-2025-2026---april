class Employee: 
    EUR_TO_RSD = 117.5
    COMPANY_NAME = "ABC"

    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
    
    def convertSalaryToEUR(self):
        return self.salary / Employee.EUR_TO_RSD
        
    def display_info(self):
        print(f"[{Employee.COMPANY_NAME}] {self.name}, {self.position} - {self.salary}")       
    
    def __str__(self):
        return f"[Employee]: {self.name}, {self.position} - {self.salary}"
     
    
em1 = Employee("Petar Petrovic", "Software Developer", 120000)
em2 = Employee("Marko Petrović", "Project Manager", 150000)
em3 = Employee("Jelena Nikolić", "Data Analyst", 110000)

em1.display_info()
em2.display_info()
em3.display_info()

print(em1)

print("Kurs:" + str(Employee.EUR_TO_RSD))
print("Kurs em1 : " + str(em1.EUR_TO_RSD))
print("Kurs em2 : " + str(em2.EUR_TO_RSD))
print("Kurs em3 : " + str(em3.EUR_TO_RSD))

Employee.EUR_TO_RSD = 118 #azurira vrednost klasnog ili static polja

print("Kurs:" + str(Employee.EUR_TO_RSD))
print("Kurs em1 : " + str(em1.EUR_TO_RSD))
print("Kurs em2 : " + str(em2.EUR_TO_RSD))
print("Kurs em3 : " + str(em3.EUR_TO_RSD))


em1.EUR_TO_RSD = 120 #python je kreirao novo instancno polje koje je vezano samo za em1 instancu

print("Kurs:" + str(Employee.EUR_TO_RSD))
print("Kurs em1 : " + str(em1.EUR_TO_RSD))
print("Kurs em2 : " + str(em2.EUR_TO_RSD))
print("Kurs em3 : " + str(em3.EUR_TO_RSD))
# !!!!!! 
Employee.EUR_TO_RSD = 130 #azurira vrednost klasnog ili static polja
print("Kurs:" + str(Employee.EUR_TO_RSD))
print("Kurs em1 : " + str(em1.EUR_TO_RSD))
print("Kurs em2 : " + str(em2.EUR_TO_RSD))
print("Kurs em3 : " + str(em3.EUR_TO_RSD))

print(em1.convertSalaryToEUR())
print(em2.convertSalaryToEUR())
print(em3.convertSalaryToEUR())