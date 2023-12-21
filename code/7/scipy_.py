#sample(import)
import scipy
#end-sample
import matplotlib.pyplot as plt
import numpy as np

#sample(minimize)
f = lambda x: 2*x**2 - 3*x + 1
res = scipy.optimize.minimize(f, 0)
print(res)
#end-sample

x = np.linspace(-1, 2.5, 100)   
plt.plot(x, f(x))
plt.savefig("img/7/minimize.png")
plt.show()

#sample(interpolate)
tag = [1, 7, 16, 20]                  # Tag im November
stromzaehler = [78, 104, 121, 130]    # kWh
f = scipy.interpolate.interp1d(tag, stromzaehler)
print(f(2))                           # 82.333 kWh am 2. November
#end-sample

x = np.linspace(1, 20, 21)   
plt.plot(x, f(x))
plt.savefig("img/7/interpolate.png")
plt.show()

#sample(extrapolate)
f = scipy.interpolate.interp1d(tag, stromzaehler, 
                               kind="cubic",
                               bounds_error=False, 
                               fill_value="extrapolate") 
print(f(30))                          # 188.7 kWh am 30. November
#end-sample

x = np.linspace(1, 30, 31)   
plt.plot(x, f(x))
plt.savefig("img/7/extrapolate.png")
plt.show()

#sample(fsolve)
f = lambda x: 2*x**2 - 3*x - 2
res = scipy.optimize.fsolve(f, 0)
print(res)                            # [-0.5]
res = scipy.optimize.fsolve(f, [0, 1])
print(res)                            # [-0.5, 2.]
#end-sample

x = np.linspace(-1, 2.5, 100)
plt.plot(x, f(x))
plt.axhline(0, color='black', linestyle='-')
plt.plot(res, f(res), "ro")
plt.savefig("img/7/fsolve.png")
plt.show()

