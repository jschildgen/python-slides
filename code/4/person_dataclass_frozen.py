from dataclasses import dataclass

@dataclass(frozen=True)    # frozen=True: Objekte sind unveränderlich
class Person:
    name: str
    alter: int

person1 = Person("Peter", 30)
person2 = Person("Ute", 25)

personen = { person1, person2 } # verwendet __hash__
print(personen)                 # verwendet __repr__