class Konto:
  next_kontonummer = 1

  def __init__(self):
    self.kontonummer = Konto.next_kontonummer
    Konto.next_kontonummer += 1

a = Konto()
b = Konto()
c = Konto()
print(a.kontonummer)  # 1
print(b.kontonummer)  # 2
print(c.kontonummer)  # 3