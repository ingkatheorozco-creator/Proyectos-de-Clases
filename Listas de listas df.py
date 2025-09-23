#DataFrame(data=listas, index=filas, columns=columnas, dtype=tipos)
import pandas as pd
'''
lst=[['Juan',23,70.5],['Carla',28,56.7],['Judith',25,51.2]]
df = pd.DataFrame(lst, columns=['nombre', 'edad', 'peso'],index = ['id1','id2','id3'])
print(df)

'''

S1 = pd.Series(['Juan', 'Carla', 'Judith'], index=['id1','id2','id3'])
S2 = pd.Series([23,28,25], index=['id1','id2','id3'])
S3 = pd.Series([70.5,56.7,51.2], index=['id1', 'id2', 'id3'])
d1={'nombre':S1, 'edad':S2, 'peso':S3}
df1=pd.DataFrame(d1)
print(df1)

