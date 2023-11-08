zahlen = { 7, 3, 5 }
zahlen.add(4)
zahlen.add(3)  # schon drin => wird nicht eingefügt
zahlen.remove(5)
print(zahlen)  # {3, 4, 7}

x = 4
if x in zahlen:
    print("Juhu! Lottogewinn!")

for z in zahlen:
    print(z)

# len, min, max, sum, ... wie bei Listen