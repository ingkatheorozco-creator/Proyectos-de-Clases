import datetime
ahora=datetime.datetime.now()
print(ahora)  #Salida: 2024-06-17 12:34:56 ejemplo   

print(ahora.strftime("%Y-%m-%d"))  #Salida: 2024-06-17

fecha1=datetime.datetime(2025,1,20)    
fecha2=datetime.datetime(2024,12,25)
diferencia=fecha1-fecha2    
print(diferencia.days)
