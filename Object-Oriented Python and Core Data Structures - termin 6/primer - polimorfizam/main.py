from data_analyst import DataAnalyst
from sales_manager import SalesManager
from intern import Intern

alice = SalesManager("Alice", "alice@gmail.com", 100000)
bob = DataAnalyst("Bob", "bob@gmail.com", "Python")
charlie = Intern("Charlie", "charlie@gmail.com", "Market Research")

alice.send_email("Hello", "How are you?")
bob.send_email("Hello", "How are you?")
charlie.send_email("Hello", "How are you?")
