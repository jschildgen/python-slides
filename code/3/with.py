# sample(with)
with open("gedicht.txt", "rt") as f:
  for line in f:
    print(line, end='')
  print()
# end-sample

# sample(try)
try:
  with open("gedicht.txt", "rt") as f:
    for line in f:
      print(line, end='')
    print()
except:   # fängt alle Exceptions ab
  print("Datei-Lesen fehlgeschlagen.")
# end-sample