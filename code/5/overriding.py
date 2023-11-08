class Person:
  name: str
  alter: int

  def __init__(self, name: str) -> None:
    self.name = name
    self.alter = 0

  def erhoehe_alter(self) -> None:
    self.alter += 1

  # sample(pers_details)
  def details(self):
    return f"{self.name} ({self.alter})"
  # end-sample

class Studierender(Person):
  matrikelnr: int

  # sample(stud_init)
  def __init__(self, name, matrikelnr):
    super().__init__(name)
    self.matrikelnr = matrikelnr
  # end-sample

  # sample(stud_details)
  def details(self):
    return str(self.matrikelnr) + " / " + super().details()
  # end-sample

  def super_beispiel(self):
    # sample(super_beispiel)
    s1 = self.details();             # 555123 / Ute (19)
    s2 = super().details();          # Ute (19)
    # end-sample
    print(s1)
    print(s2)

# sample(objects)
p = Person("Peter")
p.alter = 20
s = Studierender("Ute", 555123)
s.alter = 19

personen = [p, s]
for person in personen:
  print(person.details())
# end-sample

s.super_beispiel()