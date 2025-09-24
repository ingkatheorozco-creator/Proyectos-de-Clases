import pandas as pd

S1 = pd.Series(['Juan', 'Carla', 'Judith', 'Andres'] , index=['id1','id2','id3','id4'])
S2 = pd.Series([23.0, 28.0, 25.0,29.0], index=['id1','id2','id3','id4'])
S3 = pd.Series([70.5, 56.7, 51.2, 84.2], index=['id1','id2','id3','id4'])
S4 = pd.Series([1.84, 1.65, 1.69, 1.78], index=['id1','id2','id3','id4'])

d3={'Nombre':S1, 'Edad':S2, 'Peso':S3, 'Altura':S4}
df3=pd.DataFrame(d3)
print(df3)

print(df3.iloc[0,0])
print(df3.iloc[1])

print(df3.loc['id2','Nombre'])
print(df3.loc['id1'])
print(df3.loc['id1', ['Nombre','Peso']])

df3 ['IMC'] = df3['Peso']/df3['Altura']**2
print(df3)


df3.name = 'Datos clinicos'
print(df3.name)
print(df3.size)
print(df3.shape)
print(df3.columns)
print(df3.index)
print(df3.head(2))
print(df3.dtypes)