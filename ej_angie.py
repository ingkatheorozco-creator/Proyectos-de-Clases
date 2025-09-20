def saludar(nombre):
    print(f"Hola, {nombre}!")

# Llamada
saludar("Angie")

#----------------------------------------
def suma (a,b):
    return a + b

# Llamada - ARGUMENTOS POSICIONALES

resultado = suma(3,5)
print (resultado)

# Llamada - ARGUMENTOS DE PALABRA CLAVE

resultado = suma(a =10, b = 7)

#_______________________________________

resultado = 0
def promedio(al1,al2,al3,al4,al5):
    suma = al1+al2+al3+al4+al5
    return suma / 5

resultado = promedio(5,4,3,2,5)
print("El promedio de la clese es ", resultado)

#----------------------------------------

def prom (clase):
    return sum(clase) / len(clase)

clase = [7,8,9,7,5]
resultado = prom(clase)
print ("El promedio de la clase es ",resultado)

#----------------RAIZ CUADRADA------------------------

import math
print(math.sqrt(16))

#--------------LOGARITMOS-------------

print(math.log(100,10))
print(type(math.log(100,10)))
#--------------REDONDEO-Inferior---------------
print (math.floor(3.7))


#-------------REDONDEO -Superior----------------
print(math.ceil(3.7))

