#koristite employee.py
from employee import Employee

#napravite listu objekata tipa Employee
employees = []

#pitajte korisnika da unese podatke za 3 objekta tipa Employee
for i in range(3):
    name = input(f"Unesite ime zaposlenog {i+1}: ")
    position = input(f"Unesite poziciju zaposlenog {i+1}: ")
    salary = float(input(f"Unesite platu zaposlenog {i+1}: ")) 
    e = Employee(name, position, salary)
    # stavite objekte u listu
    employees.append(e)
    
#prodjite i ispisite sve elemente liste
print("- - - SVI ZAPOSLENI - - -")
for e in employees:
    e.display_info()
    
#izracunajte prosecnu platu, samo validnih plata u listi
sum_salary = 0
valid_salary_counter = 0
for e in employees:
    if(Employee.isValidSalary(e.salary)):
        sum_salary += e.salary
        valid_salary_counter += 1
  
if valid_salary_counter > 0:
    avg_salary = sum_salary / valid_salary_counter
    print(f"Prosecna plata: {avg_salary}")
else:
    print("Niste uneli ni jednu validnu platu. Prosek je 0.")
