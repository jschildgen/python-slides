while True:
  anzahl_str = input("Wie viele Zahnbürsten möchten Sie bestellen? ")
  try:
    anzahl = int(anzahl_str)
    break
  except ValueError:
    print("Das ist keine gültige Zahl")

print(f"OK, {anzahl} Zahnbürsten sind unterwegs!")