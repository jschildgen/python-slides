import sys

print(sys.argv)  # ['meinprogramm.py', 'test', '8', 'Hallo']

print("Anzahl Argumente:", len(sys.argv))     # 4
print("Scriptname:", sys.argv[0])             # meinprogramm.py
print("Erstes Argument:", sys.argv[1])        # test
print("Zweites Argument:", int(sys.argv[2]))  # 8
print("Drittes Argument:", sys.argv[3])       # Hallo
print("Argumente:", sys.argv[1:])  # ['test', '8', 'Hallo']
