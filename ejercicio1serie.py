import pandas as pd

serie = pd.Series([10,20,30,40])
print(serie)


'''



'''

serie= pd.Series([10,20,30,40], index=['A', 'B', 'C', 'D' ])
print(serie)

print(serie['A']) #Acceder a un valor especifico - Salida: 10

print(serie.mean()) #Calcular el promedio - Salida:25.0
