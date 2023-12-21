#sample(classifier)
import pandas as pd
from sklearn.tree import DecisionTreeClassifier

train = pd.read_csv("code/7/mensa.csv", sep=";", 
                    encoding="iso-8859-1", decimal=",")

# Datensatz aufteilen in Trainings- und Testdaten
test = train.sample(frac=0.2)
train = train.drop(test.index)

model = DecisionTreeClassifier()
model.fit(train[["stud", "bed"]], train["warengruppe"])

test["wg_pred"] = model.predict(test[["stud", "bed"]])
test
#end-sample
print(test)