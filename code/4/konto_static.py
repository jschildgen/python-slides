class Konto:
  def __init__(self, kontonummer):
    self.kontonummer = kontonummer
    self.kontostand = 0

  def kontostand_usd(self):
    return self.kontostand * 1.05

  def next_kontonummer_zuruecksetzen():
    Konto.next_kontonummer = 0