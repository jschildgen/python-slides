import numpy as np
import matplotlib.pyplot as plt

#sample(bar)
fig, ax = plt.subplots()
ax.bar(["A", "B", "C"], [1, 2, 3])
#end-sample
plt.savefig("img/7/plot_bar.png")
#sample(bar)
plt.show()
#end-sample

#sample(pie)
fig, ax = plt.subplots()
ax.pie([1, 2, 3], labels=["A", "B", "C"])
#end-sample
plt.savefig("img/7/plot_pie.png")
#sample(pie)
plt.show()
#end-sample