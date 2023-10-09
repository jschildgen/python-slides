# meine_mathe_library.py
def fakultaet(n):
    if n == 0:
        return 1
    else:
        return n * fakultaet(n-1)
    
def main():
    n = int(input("Gib eine Zahl ein: "))
    print(f"{n}! = {fakultaet(n)}")

if __name__ == '__main__':
    main()