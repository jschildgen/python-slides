class Person:
    def __init__(self, name, alter):
        self.name = name
        self.alter = alter

    def __hash__(self):
        return hash( (self.name, self.alter) )
    
    def __eq__(self, other):
        return (self.name, self.alter) == (other.name, other.alter)
    
    def __repr__(self):
        return f"{self.name} ({self.alter})"
    
personen = { Person("Ute", 30), Person("Kai", 25), Person("Bo", 35) }
personen.add(Person("Kai", 25))
print(personen) # {Bo (35), Kai (25), Ute (30)}