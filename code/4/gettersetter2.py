# sample(class)
class Konto:
  def __init__(self, kontonummer):
    self.__kontonummer = kontonummer
    self.__kontostand = 0

  @property
  def kontonummer(self):
    return self.__kontonummer

  @property
  def kontostand(self):
    return self.__kontostand

  @kontostand.setter
  def kontostand(self, kontostand):
    if kontostand < 0:
      raise ValueError("Muss positiv!")
    self.__kontostand = kontostand

k1 = Konto(123)
print(k1.kontonummer)   # ruft Getter auf
k1.kontostand = 100     # ruft Setter auf
# end-sample

# sample(exception1)
k1.kontostand = -1
# end-sample

# sample(exception2)
k1.kontonummer = 124
# end-sample
