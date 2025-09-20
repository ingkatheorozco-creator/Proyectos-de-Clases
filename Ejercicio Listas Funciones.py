#Tienes una lista de valores de ventas:
[150.75,200.50,80.00,350.25,120.00]
#Necesitas una función que reciba esta lista
#y retorne un diccionario con el total, el promedio
#y el máximo de las ventas.

def valores ():
    ventas=[150.75,200.50,80.00,350.25,120.00]
    return sum(ventas)/len(ventas)
           max(ventas)

