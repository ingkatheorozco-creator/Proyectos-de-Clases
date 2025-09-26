import pandas as pd

data= {
    "Nombre":["Ana", "Luis", "Carlos", None],
    "Edad":[23,None,29,30],
    "Ciudad":["Bogota","Medellin",None,"Cali"],
}

df=pd.DataFrame(data)
print("Datos Originales:")
print(df)

#Contar valores nulos
print("\nValores Nulos por Columna:")
print(df.isnull().sum())

#Reemplazar valores nulos en "Edad" con la media
df["Edad"]= df["Edad"].fillna(df["Edad"].mean())

#Reemplazar valores nulos en "Ciudad" con un valor fijo
df["Ciudad"]=df["Ciudad"].fillna("Desconocido")

#Eliminar filas con valores nulos en "Nombre"
df=df.dropna(subset=["Nombre"])
print("\nDatos limpios:")
print(df)



