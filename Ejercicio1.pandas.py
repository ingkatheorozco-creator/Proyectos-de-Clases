import pandas as pd

#Ejercicio 1

Serie= pd.Series([100,200,300,400,500], index= ['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes'])
print(Serie['Miercoles'])
print(Serie.mean())

nueva_serie = Serie + 50

print(nueva_serie)