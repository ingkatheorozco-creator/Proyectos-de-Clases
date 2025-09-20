#Fase I

#En una encuesta se indago por la edad de un conjunto de N personas,
#se desea calcular e imprimir la edad promedio del grupo. Escriba un algoritmo
#(DFD o Pseudocodigo) que lea el número de personas (N) y que mediante una función
#se lea las edades, se calcule la edad promedio y retorne este resultado.

#Datos de entrada
#Conjunto de personas
#Edad de las personas

#Procesos
#Calcular el promedio de las edades del conjunto de personas

#Datos de salida
#Edad promedio 

#Diseño del Algoritmo
#Ingresar el número de personas
#Ingresar la edad de las personas
#Calcular la edad promedio del grupo
#Imprimir la edad promedio

N=0;
edad_N=0;
edad=[];
i=0;

N=int(input("Ingrese el número de personas: "))

while i<N:
    edad_N=int(input(f"Ingrese la edad de persona {i+1}: "))
    edad.append(edad_N)
    i=i+1

def calcular_promedio(edad):
    return sum(edad)/len(edad)
print(calcular_promedio(edad))




 