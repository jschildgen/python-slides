#sample(import)
import numpy as np
#end-sample

#sample(array)
a = np.array([1, 2, 3])                 # 1-dim. Array
b = np.array([[1, 2, 3], [4, 5, 6]])    # 2x3-Matrix
c = np.zeros((2, 3))                    # 2x3-Matrix mit Nullen
d = np.ones((2, 3))                     # 2x3-Matrix mit Einsen
e = np.identity(3)                      # 3x3-Einheitsmatrix
f = np.arange(0, 3)                     # von 0 bis 2
g = np.linspace(0, 100, 3)              # 3 Werte von 0 bis 100
#end-sample

print(a)
print(b)
print(c)
print(d)
print(e)
print(f)
print(g)

#sample(dtype)
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3.0], [4, 5, 6]])
c = np.array([1, 2, 3], dtype=float)
print(a.dtype, b.dtype, c.dtype)        # int64 float64 float64
#end-sample

#sample(attributes)
print(a.shape)          # (3,)    (3 Zeilen)
print(b.shape)          # (2, 3)  (2 Zeilen, 3 Spalten)
print(a.ndim, b.ndim)   # 1 2     (Dimensionen)
print(a.size, b.size)   # 3 6     (Anzahl Elemente)
#end-sample

#sample(indexing)
a = np.array([1, 2, 3])
b = np.array([[1, 2, 3], [4, 5, 6]])

print(a[0])             # 1
print(a[0:2])           # [1 2]

print(b[0, 1])          # 2
print(b[1, 1:])         # [5 6]

print(b[0])             # [1 2 3]  (ganze 1. Zeile)
print(b[:, 0])          # [1 4]    (ganze 1. Spalte)

b[0, 2] = 43            # Wert zuweisen

print(b[b % 2 == 0])    # Gerade Zahlen [2 4 6]
b[b % 2 == 0] *= 2      # Gerade Zahlen verdoppeln
#end-sample

print(b)

print("sample(operations)")
#sample(operations)
a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape((2, 3))             # 2 Zeilen, 3 Spalten
c = a[0:3]                        # [1 2 3] (Referenz)
d = a[0:3].copy()                 # [1 2 3] (Kopie)
e = np.transpose(b)               # Transponiert (3x2)

a[0] = 42                         # hat auch Effekt auf b und c!
print(b)                          # [[42  2  3] [ 4  5  6]]
print(c)                          # [42  2  3]
print(d)                          # [1 2 3]
print(e)                          # [[42  4] [ 2  5] [ 3  6]]
#end-sample

print(a)

#sample(math)
a = np.array([1, 2, 3])
print(a + 1)             # [2 3 4]
print(a * 2)             # [2 4 6]
print(a ** 2)            # [1 4 9]
print(a + a)             # [2 4 6]
print(a * a)             # [1 4 9] (Elementweise)
print(a.dot(a))          # 14 (Skalarprodukt)
print(a.sum())           # 6
print(a.mean())          # 2.0
print(a.std())           # 0.816496580928 (Standardabweichung)
#end-sample

#sample(math2)
b = np.array([[1, 2, 3], [4, 5, 6]])
print(b + 1)             # [[2 3 4] [5 6 7]]
print(b * 2)             # [[ 2  4  6] [ 8 10 12]]
print(b ** 2)            # [[ 1  4  9] [16 25 36]]
print(b + b)             # [[ 2  4  6] [ 8 10 12]]
print(b * b)             # [[ 1  4  9] [16 25 36]] (Elementweise)
print(b @ a)             # [14 32] (Matrix-Vektor-Produkt)
c = np.array([[1, 2], [3, 4], [5, 6]])
print(b @ c)             # [[22 28] [49 64]] (Matrix-Mult.)
#end-sample

#sample(functions)
a = np.array([0, np.pi/6, np.pi/2])
print(np.sin(a))                 # [0.  0.5 1. ]
#end-sample

#sample(lambda)
f = lambda x: x**2 + 2*x + 1
print(f(3))                     # 16
x = np.linspace(0, 10, 5)       # [  0.    2.5  5.     7.5  10. ]
print(f(x))                     # [  1.  12.25  66.  72.25  82. ]
#end-sample

#sample(def)
def f(x):                       # entspricht obiger Lambda-Funktion
    return x**2 + 2*x + 1   
#end-sample