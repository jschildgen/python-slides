a = 5
b = 3.3
s = "Hallo"
print(type(a))  # <class 'int'> 
print(type(b))  # <class 'float'>
print(type(s))  # <class 'str'>

if type(a) == int:
  print("a ist ein Integer")

# besser:
if isinstance(a, int):
  print("a ist ein Integer")