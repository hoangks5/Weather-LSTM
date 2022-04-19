import pandas as pd
data = pd.read_csv("MeshliumDB_sensorData-210126.csv", header=None)
df = data[[5,6,7]]
df = df.pivot_table(index=7, columns=5, values=6, aggfunc='first')
df.iloc[:9999999,:-1] = df.iloc[:9999999,:-1].fillna(0)
df.to_csv('n.csv')
print(df)