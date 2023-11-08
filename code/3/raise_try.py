def stars(password):
  if(password == None or len(password) < 5):
    raise ValueError("Ungültiges Passwort")
  return "*"*len(password)

# sample(main)
while True:
  try:
    pw = input("Wähle ein Passwort: ")
    pw_stars = stars(pw)
    break
  except ValueError:
    pass
print(pw_stars)
# end-sample
