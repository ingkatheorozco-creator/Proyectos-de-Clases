#Encontrar el mayor numero en una lista
numeros = [10, 25, 3, 45, 7, 90, 12];
i=0;
mayor=0; 

while i<6:
    if numeros[i]>mayor:
        mayor=numeros[i]
    i=i+1
print("El mayor numero es ", mayor)


#Ahora ingresando la lista por teclado
cantidad=int(input("Por favor ingrese la cantidad de numeros que desea comparar ", ))
numeros=[];
i=0;
mayor=0;
while i<cantidad:
    numero=int(input(f"Por favor ingrese el numero {i+1} ", ))
    numeros=numeros + [numero]
    if numeros[i]>mayor:
        mayor=numeros[i]
    i=i+1


print("El mayor numero es ", mayor) 