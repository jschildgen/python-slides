# Globale Variable
g = "Ich bin global"

def my_function():
  # Lokale Variable
  l = "Ich bin lokal"
  print(l)
  print(g)

# Call the function
my_function()

print(g) 
# print(l) # NameError: name 'l' is not defined
