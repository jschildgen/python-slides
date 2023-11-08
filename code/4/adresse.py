# sample(reference)
class Person:
  def __init__(self, name, 
               alter=None):
    self.name = name
    self.alter = alter
    self.adresse = None

class Adresse:
  def __init__(self, strasse, hausnummer, plz, ort):
    self.strasse = strasse
    self.hausnummer = hausnummer
    self.plz = plz
    self.ort = ort

p = Person("Peter")
p.adresse = Adresse("Holzweg", "3a", "09111", "Chemnitz")
print(f"{p.name} wohnt in {p.adresse.ort}")
# end-sample

# sample(objects)
p = Person("Peter")
u = Person("Ute")
a = Adresse("Holzweg", "3a", "09111", "Chemnitz")
p.adresse = a
u.adresse = a
# end-sample

# sample(is)
if p.adresse is u.adresse:
  print(f"{p.name} und {u.name} haben dieselbe Adresse.")
# end-sample

# sample(change)
p.adresse.hausnummer = "5"
print(f"{u.name} wohnt in der Hausnummer {u.adresse.hausnummer}")
# end-sample