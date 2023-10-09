def gauss(n):
    sum = 0
    for i in range(1, n+1):
        sum += i
    return sum
  
print(gauss(5)) 
# hier ist kein Zugriff auf die Variable i und sum möglich