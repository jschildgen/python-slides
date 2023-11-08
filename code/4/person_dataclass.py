from dataclasses import dataclass

@dataclass()
class Person:
    name: str
    alter: int

person1 = Person("Peter", 30)
person2 = Person("Ute", 25)

print(person1)                  # verwendet __str__

if person1 == person2:          # verwendet __eq__
    print("Die Personen sind gleich.")

person1.alter += 1              # Die Objekte sind veränderlich