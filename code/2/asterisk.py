# sample(entpacken)
zahlen = [1, 2, 3]

print(*zahlen)  # entspricht print(1, 2, 3)

zahlen2 = [*zahlen, 4, 5]
tupel = (*zahlen,)
liste = [*tupel]
# end-sample

# sample(packen)
def summe(*liste):
    return sum(liste)

print(summe(1, 2, 3))  # 6
# end-sample