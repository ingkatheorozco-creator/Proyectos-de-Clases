import pandas as pd

#Crear Dataframe desde un diccionario

datos = {
    'Nombre':['Ana', 'Luis', 'Carlos'],
    'Edad': [23,34,29],
    'Ciudad': ['Bogota', 'Medellin', 'Cali']
}
'''
df = pd.DataFrame(datos)
print(df)

'''
d= {'nombre':['Juan', 'Carla', 'Judith'], 'edad':[23,28,25], 'peso':[70.5,56.7,51.2]}
df = pd.DataFrame(d, index = ['id1','id2','id3'])
print(df)

