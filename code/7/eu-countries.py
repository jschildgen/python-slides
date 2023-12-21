import pandas as pd

data = pd.read_csv("code/7/eu-countries.csv", 
                   sep=";", header=None, thousands=',')
data.columns = ["ID", "Country", "Population", "Region"]
data = data.drop(columns=["ID"])
data["Population"] = data["Population"].astype(int)

west = data[data["Region"] == "Western Europe"]
print(west["Population"].sum())                      # 196146316
data.sort_values("Country")   # alphabetisch sortiert nach Land