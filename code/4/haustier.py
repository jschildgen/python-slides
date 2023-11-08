class Haustier:
  TIERART = "Hund"
  farbe = None
  def __init__(self, name):
    self.name = name

h1 = Haustier("Waldi")
h2 = Haustier("Fiffy")
print(f"{h1.name} ist ein {Haustier.TIERART}")
Haustier.farbe = "weiß"
print(f"{h1.name} ist {h1.farbe}")  # Waldi ist weiß
print(f"{h2.name} ist {h2.farbe}")  # Fiffy ist weiß
print(f"{h2.name} ist {Haustier.farbe}")  # besser so 