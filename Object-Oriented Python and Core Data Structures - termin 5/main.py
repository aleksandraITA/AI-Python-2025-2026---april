from employee import Employee


em1 = Employee("Petar Petrovic", "Software Developer", 120000)
em2 = Employee("Marko Petrović", "Project Manager", 150000)
em3 = Employee("Jelena Nikolić", "Data Analyst", 110000)

em1.display_info()
em2.display_info()
em3.display_info()

  
res = Employee.convertEURtoRSD(1000)
print(res)

print(Employee.isValidSalary(150))
print(Employee.isValidSalary(-1520))