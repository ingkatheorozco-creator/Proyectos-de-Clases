import pandas as pd
df=pd.read_csv("datos_groupby.csv")
#print(df)
#print(df["Precio Unitario"])

import matplotlib.pyplot as plt

precio= (df["Precio Unitario"])
print(precio.describe())

plt.hist(precio, bins=5, color="green", edgecolor="white")
plt.title("Distribución de Precios Unitarios")
plt.xlabel("Rango de Precios")
plt.ylabel("Frecuencia")
plt.show()
