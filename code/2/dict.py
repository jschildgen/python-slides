vorwahl = { "DE": 490, "AT": 43, "CH": 41 }
print(vorwahl["AT"])  # 43

vorwahl["DE"] = 49    # Wert ändern
vorwahl["IT"] = 39    # Schlüssel-Wert-Paar hinzufügen

print(len(vorwahl))   # 4 (Anzahl Elemente)

if "CH" in vorwahl:
    print("Die Schweiz ist dabei.")

vorwahl2 = { "DE": 49, "ES": 34, "FR": 33 }
vorwahl = vorwahl | vorwahl2 # Vereinigung (vorwahl2 hat Vorrang)
print(vorwahl)
# {'DE': 49, 'AT': 43, 'CH': 41, 'IT': 39, 'ES': 34, 'FR': 33}