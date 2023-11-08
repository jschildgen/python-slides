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

  # sample(__eq__)
  def __eq__(self, other):                      # in der Klasse Adresse
    return (self.strasse == other.strasse 
            and self.hausnummer == other.hausnummer
            and self.plz == other.plz and self.ort == other.ort)
  # end-sample

# sample(objects)
p = Person("Peter")
u = Person("Ute")
p.adresse = Adresse("Holzweg", "3a", "09111", "Chemnitz")
u.adresse = Adresse("Holzweg", "3a", "09111", "Chemnitz")
# end-sample

# sample(eq)
if p.adresse is u.adresse:
  print(f"{p.name} und {u.name} haben dieselbe Adresse.")

if p.adresse == u.adresse:
  print(f"{p.name} und {u.name} haben die gleiche Adresse.")
# end-sample