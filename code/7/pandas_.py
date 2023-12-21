#sample(import)
import pandas as pd
#end-sample

#sample(series)
s = pd.Series([1, 2, 3])
#end-sample
print(s)

#sample(dataframe)
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], columns=["A", "B", "C"])
#end-sample
print(df)

#sample(series1)
s = pd.Series([3, 9, 1, 27, 4, 11])
print(s[0])   # 3
print(s[0:2])           
print(s[s < 10])        
#end-sample

#sample(series2)
s = pd.Series([3, 9, 1], 
              index=["A", "B", "C"])
print(s["A"]) # 3
print(s["A":"B"])       
print(s[["A", "C"]])    
#end-sample


#sample(dataframe1)
df = pd.DataFrame([[1, 2, 3], [4, 5, 6]], 
                  columns=["A", "B", "C"])
print(df["A"])          # Spalte A (Series)
print(df[0:1])          # Zeile 0 (DataFrame)
print(df[["A", "C"]])   # Spalten A und C (DataFrame)
print(df[df["A"] < 4])  # Zeilen, bei denen A < 4 ist
#end-sample

#sample(dataframe2)
print(df.drop_duplicates())    # Doppelte Zeilen entfernen
print(df.head())               # Nur erste 5 Zeilen
print(df.tail())               # Nur letzte 5 Zeilen
print(df.sample(2))            # Zufällige 2 Zeilen
print(df.nlargest(2, "A"))     # 2 Zeilen, die größtes A haben
#end-sample

#sample(dataframe3)
df = df.set_index("A")  # Was A war, ist nun der Index

df = (df.rename(columns={"B": "Foo"})
        .sort_values("C")       # Sortieren nach Alter
        .sort_index()           # Sortieren nach Index
        .drop(columns=["C"])    # Spalten entfernen
        .drop(index=[1])        # Zeile entfernen
        .reset_index())         # Indizes zurücksetzen
#end-sample

#sample(loc)
print(df.loc[0])        # Zeile mit Index 0
print(df.loc[0:1])      # Zeilen mit Index 0 und 1
print(df.loc[0, "Foo"]) # Wert in Zeile 0, Spalte Foo
print(df.loc[0:1, "Foo"]) # Werte in Zeilen 0 und 1, Spalte Foo
print(df.loc[df["Foo"] == 2]) # Zeilen, bei denen Foo == 2 ist
print(df.loc[(df["Foo"] == 5) & (df["A"] == 4)])
#end-sample

print(df)