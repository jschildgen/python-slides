try:
  f = open("gedicht.txt", "rt")
  for line in f:
    print(line, end='')
  print()
  f.close()
except FileNotFoundError as err:
  print("Die Datei existiert nicht.")
  print(err)  # [Errno 2] No such file or directory: 'gedicht.txt'
except PermissionError as err:
  print("Rechte zum Zugriff auf die Datei fehlen.")
  print(err)  # [Errno 13] Permission denied: 'gedicht.txt'
except BaseException as err:
  print("Irgendetwas anderes ist schief gelaufen.")
  print(err)