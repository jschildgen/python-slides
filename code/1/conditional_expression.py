# sample(cond)
SPRACHE = "DE"
begruessung = "Guten Tag" if SPRACHE == "DE" else "Hello"
print(begruessung)
# end-sample

# sample(if)
if SPRACHE == "DE":
    begruessung = "Guten Tag"
else:
    begruessung = "Hello"
# end-sample