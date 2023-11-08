def stars(password):
  if(password == None or len(password) < 5):
    raise ValueError("Ungültiges Passwort")
  return "*"*len(password)

if __name__ == '__main__':
  print(stars("Hallo"))   # *****
  print(stars("hi"))      # Error