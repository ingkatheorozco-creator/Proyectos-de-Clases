mi_diccionario = {
    "nombre": "Jhon",
    "edad": 25,
    "ciudad": "New york"
}

#Acceso a los valores mediante las claves
print(mi_diccionario["nombre"])  # Salida: Jhon
print(mi_diccionario.get("edad"))  # Salida: 25 
print(mi_diccionario["edad"])  # Salida: 25

#Modificacion de los valores
mi_diccionario["edad"] = 26
print(mi_diccionario)  # Salida: {'nombre': 'Jhon', 'edad   : 26, 'ciudad: 'New york'}

#Agregar nuevos pares clave-valor
mi_diccionario["profesion"] = "Programador"
print(mi_diccionario)  # Salida: {'nombre': 'Jhon', 'edad': 26, 'ciudad': 'New york', 'profesion': 'Programador'}   

#Eliminar un elemento
del mi_diccionario["ciudad"]
print(mi_diccionario)  # Salida: {'nombre': 'Jhon', 'edad': 26, 'profesion': 'Programador'}

#Mostrar el diccionario completo
print("Diccionario actualizado:", mi_diccionario)  # Salida: Diccionario actualizado: {'nombre': 'Jhon', 'edad': 26, 'profesion': 'Programador'}

