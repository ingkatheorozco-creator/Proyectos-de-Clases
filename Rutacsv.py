import pandas as pd

#Cargar un archivo CSV

#df= pd.read_csv("C:/Users/Usuario/Documents/Ejercicios/airports.csv")

#print(df)

#df=pd.read_csv("airports.csv",usecols=["id","name","iso_country","continent"])
#print(df)

#df=pd.read_csv("airports.csv", nrows=15)
#print(df)

#df=pd.read_excel("airports1.xlsx")
#print(df)

print("/n")

#df= pd.read_excel("airports1.xlsx", sheet_name="Hoja1")
#print(df)

#df=pd.read_excel("airports1.xlsx",usecols="A:C")
#print(df)

#df=pd.read_excel("airports1.xlsx", nrows=10)
#print(df)

df=pd.read_excel("airports1.xlsx", skiprows=2)
print(df)

#df.to_csv("exportado.csv", index=False)

df.to_csv("exportado.csv", sep=";")

df.to_csv("exportado.csv",)