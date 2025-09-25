#Producto: "Manzana", "Banana", "Cereza"
#Precio: 2.5,1.8,3.0
#Cantidad: 10,15,8
#Muestra las dos primeras filas
#Accede a columna Precio y calcula el precio total de todos los productos(multiplica precio por cantidad y 
#suma el total)
#Agrega una nueva columna Precio total que almacene el calculo del precio total para cada producto

import pandas as pd

S1 = pd.Series(['Manzana', 'Banana', 'Cereza'] , index=['id1','id2','id3'])
S2 = pd.Series([2.5, 1.8, 3.0], index=['id1','id2','id3'])
S3 = pd.Series([10,15,8], index=['id1','id2','id3'])

df={'Producto':S1, 'Precio':S2, 'Cantidad':S3}
df=pd.DataFrame(df)

print(df.head(2))

Precio_total_general = (df["Precio"] * df["Cantidad"]).sum()
print(Precio_total_general)

df ['Precio Total'] = df['Precio']*df['Cantidad']
print(df)