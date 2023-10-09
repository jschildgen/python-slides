s = "Dies ist ein Test"

# Zugriff auf Zeichen, Substring/Slice
print(s[0])    # Erstes Zeichen (D)
print(s[-1])   # Letztes Zeichen (t)
print(s[0:4])  # Erste vier Zeichen (Dies)
print(s[:4])   # Erste vier Zeichen (Dies)
print(s[5:])   # Ab dem sechsten Zeichen (ist ein Test)
print(s[-4:])  # Die letzten vier Zeichen (Test)

# Methoden
print(s.lower())     # dies ist ein test
print(s.upper())     # DIES IST EIN TEST
print(s.replace("ein", "kein"))  # Dies ist kein Test
print(s.split(" "))  # ['Dies', 'ist', 'ein', 'Test']
print(s.find("ist")) # 5 