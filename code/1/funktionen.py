def quadrat(x):               # Funktion mit einem Parameter
    return x * x

def fuenf():                  # Funktion ohne Parameter
    return 5

def hello(name):              # Funktion ohne Rückgabewert
    print(f"Hello {name}!")

def hallo(name="Welt"):      # Funktion mit optionalem Parameter
    print(f"Hallo {name}!")

print(quadrat(5)) # 25
print(fuenf())    # 5
hello("Peter")    # Hello Peter!
hallo()           # Hallo Welt!
hallo("Ute")      # Hallo Ute!