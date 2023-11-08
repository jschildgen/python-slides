zahlen = [7, 3, 5, 9, 4, 6, 8]

gerade = [z for z in zahlen if z % 2 == 0]
print(gerade)    # [4, 6, 8]

quadrate = [z*z for z in zahlen]
print(quadrate)  # [49, 9, 25, 81, 16, 36, 64]

res = [z*10 for z in zahlen if z % 2 == 1 and z > 5]