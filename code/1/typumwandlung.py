a = "5"
b = "3.3"
print(a + b)                   # 53.3 (String-Konkatenation)
print(int(a) + float(b))       # 8.3 (Addition von Zahlen)

spannung = 230
print(str(spannung) + "V")   # 230V
print("%dV" % spannung)      # 230V

n = input("Wie alt bist du? ")
print("Ui, dann bist du ja nächstes Jahr schon %d" % (int(n)+1))
for i in range(int(n)):      # 0, 1, 2, 3, 4, ..., n-1
  print(i)
