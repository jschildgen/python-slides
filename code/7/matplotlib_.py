#sample(import)
import numpy as np
import matplotlib.pyplot as plt
#end-sample

#sample(plot)
x = np.linspace(-10, 10, 100)   
f = lambda x: x**2 + 10         
plt.plot(x, f(x))
#end-sample
plt.savefig("img/7/plot_x2.png")
#sample(plot)
plt.show()
#end-sample

x = np.linspace(-10, 10, 100)   
f = lambda x: x**2 + 10 
#sample(fmt)        
plt.plot(x, f(x), 'r--')    # r: red
#end-sample
plt.savefig("img/7/plot_x2--.png")
plt.show()

plt.figure()

#sample(plot2)
x = np.linspace(-10, 10, 100)   
f = lambda x: x**2 + 10
g = lambda x: 100 * np.sin(x) + 100
plt.plot(x, f(x), x, g(x))
#end-sample
plt.savefig("img/7/plot_x2_sin.png")
#sample(plot2)
plt.show()
#end-sample

#sample(plot3)
plt.figure()        # neues Diagramm
plt.plot(x, f(x))
plt.plot(x, g(x))
plt.show()
#end-sample

plt.figure()

#sample(subplots)
fig, ax = plt.subplots()
ax.grid()                   # Gitternetzlinien 
ax.plot(x, f(x), label="f(x)", color="red")
ax.plot(x, g(x), label="g(x)", color="blue")
ax.legend()                 # Legende
ax.set_title("Beispiel 1")
ax.set_xlabel("x")          # Beschriftung x-Achse
ax.set_ylabel("y")          # Beschriftung y-Achse
#end-sample
plt.savefig("img/7/plot_subplots.png")
#sample(subplots)
plt.show()
#end-sample