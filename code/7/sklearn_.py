#sample(import)
from sklearn import linear_model
import pandas as pd
#end-sample

import matplotlib.pyplot as plt

#sample(linear_regression)
data = pd.DataFrame({'x': [1, 2, 3, 4, 5, 8], 
                     'y': [1, 3, 2, 3, 5, 5]})

model = linear_model.LinearRegression()
model.fit(data[['x']], data[['y']])

# Vorhersage für x = 7
print(model.predict(pd.DataFrame({'x': [7]})))   # [[4.9297]]
#end-sample

# draw
plt.scatter(x, y)
plt.plot(x, model.predict(x), color="red")
plt.savefig("img/7/linear_regression.png")
plt.show()
