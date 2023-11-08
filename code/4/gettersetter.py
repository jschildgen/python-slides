class Konto:
  def __init__(self, kontonummer):
    self.kontonummer = kontonummer
    self.kontostand = 0

  # sample(Getter)
  @property
  def kontostand(self):
    return self.__kontostand
  # end-sample

  # sample(Setter)
  @kontostand.setter
  def kontostand(self, kontostand):
    if kontostand < 0:
      raise ValueError("Muss positiv!")
    self.__kontostand = kontostand
  # end-sample

# sample(normal)
k1 = Konto(123)
k1.kontostand = 100   # Attribut setzen
print(k1.kontostand)  # Attribut auslesen
# end-sample
