import pandas as pd

df=pd.read_csv("Registro de ventas.csv")
print(df)

df.to_excel("exportado_registro1.xlsx", index=False)
