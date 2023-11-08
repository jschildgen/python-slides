try:
  f = open("gedicht.txt", "rt")
  for line in f:
    print(line, end='')
  print()
except FileNotFoundError:
  pass
finally:
  if 'f' in locals():
    f.close()