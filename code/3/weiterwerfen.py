def teilen(a, b):
  return a/b

def durchschnitt(l):
  return teilen(sum(l), len(l))

if __name__ == '__main__':
  zahlen = [5, 9, 10, 6]
  print(durchschnitt(zahlen)) # 7.5
  leer = []
  print(durchschnitt(leer))   # Error