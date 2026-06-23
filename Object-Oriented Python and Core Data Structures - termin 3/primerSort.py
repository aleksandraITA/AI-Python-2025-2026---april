numbers = [1, 5, 7, 9, 2, 3, 4, 11]
numbers.sort()
print(numbers)

# drugi primer
students = [
    ("Ana", 90),
    ("Marko", 75),
    ("Jovan", 85)
]

students.sort(key=lambda student: student[1], reverse=True)
print(students)
