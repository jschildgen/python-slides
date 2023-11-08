# sample(classes)
class Person:
  name: str
  alter: int

  def __init__(self, name: str) -> None:
    self.name = name
    self.alter = 0

  def erhoehe_alter(self) -> None:
    self.alter += 1

class Studierender(Person):
  matrikelnr: int

  def __init__(self, name: str, matrikelnr: int) -> None:
    super().__init__(name)
    self.matrikelnr = matrikelnr
# end-sample

# sample(objects)
p = Person("Peter")
s = Studierender("Ute", 555123)
# end-sample

# sample(print)
print(p.name)                         # Peter
print(f"{s.name} ({s.matrikelnr})")   # Ute (555123)
# end-sample

# sample(isinstance)
if isinstance(s, Studierender):
  print(f"{s.name} studiert.")

if isinstance(s, Person):
  print(f"{s.name} lebt.")
# end-sample

# sample(wer_ist_aelter)
def wer_ist_aelter(p1: Person, p2: Person) -> bool:
  return p1.alter > p2.alter

p.alter = 20
s.alter = 19

if wer_ist_aelter(p, s):
  print(f"{p.name} ist älter als {s.name}")
# end-sample