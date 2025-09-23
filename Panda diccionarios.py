import pandas as pd

dicc = {'mangos':20, 'naranjas': 33, 'fresas':52, 'peras':20}
s = pd.Series(dicc)
'''
print(s)


'''
print("-"*30)

S = pd.Series(dicc, index = {'mangos', 'naranjas', 'fresas', 'peras', 'kiwis'})
print (S)
'''
print (S['mangos'])

print (S[['mangos', 'fresas']])

print (S[0])

print (S[1:3])

print (S[2:])
'''

S.name = 'Frutas de la compra'
print(S.count ())
print(S.sum())
print(S.min())
print(S.mean())
print(S.describe())








