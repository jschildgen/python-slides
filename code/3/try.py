anzahl_str = input("Wie viele Zahnbürsten möchten Sie bestellen? ")
try:
  anzahl = int(anzahl_str)
except ValueError:
  print("Das ist keine gültige Zahl")