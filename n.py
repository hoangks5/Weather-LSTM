import pandas as pd
data = pd.read_csv("MeshliumDB_sensorData-210126.csv", header=None)
df = data[[5,6,7]]
df.head()
df = df.pivot_table(index=7, columns=5, values=6, aggfunc='first')
df.head()
df.iloc[:5,:-1] = df.iloc[:5,:-1].fillna(0)
df.head()
df.rename(index={0:"Date time"})
df.head()
