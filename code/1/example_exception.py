try:
  with open("beispiel.txt", "r", encoding="utf-8") as f:
    content = f.read()
  print(content)
except FileNotFoundError:
  print("Datei nicht gefunden!")