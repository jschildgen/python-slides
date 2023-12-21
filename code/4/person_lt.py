class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def __lt__(self, other):
        return self.alter < other.alter

person1 = Person("Peter", 30)
person2 = Person("Ute", 25)
person3 = Person("Katja", 35)

if person1 < person2: 
    print(f"{person1.name} ist jünger als {person2.name}")

personen_liste = [person1, person2, person3]
personen_liste.sort()

for person in personen_liste:
    print(f"Name: {person.name}, Alter: {person.alter}")
