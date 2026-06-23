python_students = {"Ana", "Marko", "Jelena", "Nikola", "Sara"}

ai_students = {"Sara", "Nikola", "Stefan", "Mina", "Ana"}

#nadji sve studente koji su slusali obe radionice

print(python_students.intersection(ai_students))


# pronašli učenike koji su bili samo na Python radionici

print(python_students.difference(ai_students))

# pronašli učenike koji su bili samo na AI radionici
print(ai_students.difference(python_students))


# studenti koji su slusali barem jednu radionicu
svi_studenti = ai_students.union(python_students)
print(svi_studenti)
