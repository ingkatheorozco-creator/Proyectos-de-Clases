import pandas as pd

df=pd.read_csv("Libro1ventas.csv", sep=";")

print(df['TOTAL'])

print(df['TOTAL'].sum())


#df.to_excel("Libro1.xlsx", index=True)
#print(df)

