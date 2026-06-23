import employee


em1 = employee.Employee("Petar Petrovic", "Software Developer", 120000)
em2 = employee.Employee("Marko Petrović", "Project Manager", 150000)
em3 = employee.Employee("Jelena Nikolić", "Data Analyst", 110000)

em1.display_info()
em2.display_info()
em3.display_info()

  
res = employee.Employee.convertEURtoRSD(1000)
print(res)

print(employee.Employee.isValidSalary(150))
print(employee.Employee.isValidSalary(-1520))