import math           # Alles aus dem Modul math importieren
from random import randint   # Nur eine Funktion importieren
import numpy as np    # Modulimport mit Alias

print(math.sqrt(9))   # Wurzel aus 9 ist 3
print(randint(1, 10)) # Zufallszahl zwischen 1 und 10
matrix1 = np.array([[1, 2], [3, 4]])
matrix2 = np.array([[5, 6], [7, 8]])
print(matrix1 + matrix2)
