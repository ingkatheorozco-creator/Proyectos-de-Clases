import datetime

fecha_str = "2025-01-25"
fecha = datetime.datetime.strptime(fecha_str, "%Y-%m-%d")
print(fecha) #Salida: 2025-01-25 00:00:00


fechas=["2025-01-01","2025-02-15","2025-02-28"]
formateadas=[datetime.datetime.strptime(fecha,"%Y-%m-%d") for fecha in fechas]
meses=[fecha.strftime("%B") for fecha in formateadas]
print(meses)

