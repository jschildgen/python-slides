# sample(while)
i = 1
while i <= 10:
    print(i)
    i += 1
# end-sample

# sample(whiletrue)
i = 1
while True:
    print(i)
    i += 1
    if i > 10:
        break           # Rausspringen aus der Schleife
# end-sample

# sample(for)
for i in range(10):     # 0 bis 9
    print(i)

for i in range(1, 11):  # 1 bis 10
    print(i)
# end-sample

# sample(break)
for i in range(10):
    if i == 5:
        break
    print(i)
# end-sample

# sample(continue)
for i in range(10):
    if i == 5:
        continue
    print(i)
# end-sample