#Ordenar una lista

numeros = [5, 2, 9, 1, 5, 6]
numeros.sort()
print(numeros)  # Imprime: [1, 2, 5, 5, 6, 9]
#Ordenar una lista en orden inverso
numeros.sort(reverse=True)
print(numeros)  # Imprime: [9, 6, 5, 5, 2, 1]
#Ordenar una lista sin modificar la original
numeros1 = [4,2,8,1]
ordenados = sorted(numeros1) 
print(ordenados)  # Imprime: [1,2,4,8]
print(numeros)  # Imprime: [4,2,8,1]
numeros1.sort(reverse=True)
print(numeros1)  # Imprime: [8,4,2,1]  

#Ordenar una lista de mezcla de tipos de datos
mixfrutas = ["manzana", 10000, "naranja", "banana", "kiwi",1,3.5]   
#mixfrutas.sort()
#print(mixfrutas)  # No se puede ordenar una lista con mezcla de tipos de datos
#TypeError: '<' not supported between instances of 'int' and 'str'

#Concatenar listas
lista1 = [1, 2, 3]
lista2 = [4, 5, 6]
combinada = lista1 + lista2
print(combinada)  # Imprime: [1, 2, 3, 4, 5, 6]

#Iterar sobre una lista
colores2 = ["rojo", "azul", "verde"]
for color in colores2:
    print(color)

#Repetir elementos en una lista
repetidos = ["hola"] * 3
print(repetidos)  # Imprime: ['hola', 'hola', 'hola']

print([3]*5)  # Imprime: [3, 3, 3, 3, 3]



