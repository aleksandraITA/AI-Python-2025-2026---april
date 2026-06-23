#Kreirajte klasu Employee sa sledećim karakteristikama:
# polja:name, position i salary
# dodajte metod za ispis objekta
# a onda napravite 3 instance sa konkretnim podacima
# ispisite detalje svakog objekta

class Employee: 
    def __init__(self, name, position, salary):
        self.name = name
        self.position = position
        self.salary = salary
            
    def display_info(self):
        print(f"{self.name}, {self.position} - {self.salary}")       
    
    def __str__(self):
        return f"[Employee]: {self.name}, {self.position} - {self.salary}"
     
    
em1 = Employee("Petar Petrovic", "Software Developer", 120000)
em2 = Employee("Marko Petrović", "Project Manager", 150000)
em3 = Employee("Jelena Nikolić", "Data Analyst", 110000)

print(type(em1.name))
print(type(em1))

#print(f"{em1.name}, {em1.position} - {em1.salary}")
#print(f"{em2.salary}, {em1.position} - {em2.name}")

em1.display_info()
em2.display_info()
em3.display_info()

print(em1)
