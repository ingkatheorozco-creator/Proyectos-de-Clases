import pandas as pd

data = { 
    "ID": ["1","2","3"],
    "Fecha": ["2025-01-01","2025-02-15","No disponible"],
    "Monto": ["1000.5","2000","Invalido"]
}
df=pd.DataFrame(data)
print(df)

#Convertidor "ID" a entero
df["ID"] = pd.to_numeric(df["ID"], errors="coerce")
print(df)
#Convertir "Fecha" a datetime
df["Fecha"] = pd.to_datetime(df["Fecha"], errors="coerce")
print(df)
#Convertir "Monto" a flotante
df["Monto"] = pd.to_numeric(df["Monto"], errors="coerce")
print(df)