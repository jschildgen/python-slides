koordinaten = (49.003674, 12.095089)

breitengrad = koordinaten[0]
laengengrad = koordinaten[1]

lat, lon = koordinaten

a = 1
b = 2
(a, b) = (b, a)   # jetzt ist  a = 2 und b = 1
a, b = b, a       # nun wieder a = 1 und b = 2

t = (7,)          # Tupel mit nur einem Element

monat = 9
if monat in (4, 6, 9, 11):
    print("Der Monat hat 30 Tage")