colores = ["rojo", "azul", "verde"]

#Añadir al final
colores.append("amarillo")
print(colores)  # Imprime: ['rojo', 'azul', 'verde', 'amarillo']

#Insertar en una posición específica
colores.insert(1, "naranja")
print(colores)  # Imprime: ['rojo', 'naranja', 'azul', 'verde', 'amarillo']

#Comprobar si un elemento está en la lista
print("rojo" in colores)  # Imprime: True 
print("morado" in colores)  # Imprime: False 

#Eliminar un elemento por valor
colores.remove("rojo")
print(colores)  # Imprime: ['naranja', 'azul', 'verde', 'amarillo']

#Eliminar el ultimo elemento 
colores.pop()
print(colores)  # Imprime: ['naranja', 'azul', 'verde']

#Eliminar un elemento por índice
del colores[0]
print(colores)  # Imprime: ['azul', 'verde']

#Vaciar la lista
colores.clear()
print(colores)  # Imprime: [] 

#Modificar un elemento
colores = ["violeta"]
print(colores)  # Imprime: ['violeta']

#Numero de elementos
print(len(colores))  # Imprime: 1


colores1=["rojo", 1, True, "hola mundo", 3.5, 100000, -50]
print(len(colores1))  # Imprime: 7