class User:
    name = ""
    surname = ""
    email = ""
    
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
        
    def __str__(self):
        return f"Name: {self.name}, Surname: {self.surname}, Email: {self.email}"
    
user1 = User("Ana", "Petrovic", "ana@example.com")
user2 = User("Milan", "Mitrovic", "milan@example.com")

users = [user1, user2]

print(user1)
print(user2)