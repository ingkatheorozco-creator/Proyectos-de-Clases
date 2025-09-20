def edades(n):
    lista_edades=[]
    for i in range(n):
        edad_n=int(input(f"Ingrese la edad de la personas {i+1} de {n}: "))
        lista_edades.append(edad_n)
    return sum(lista_edades)/len(lista_edades)

n_personas=int(input("Ingrese la cantidad de personas: "))
print(edades(n_personas))


#Un solo argumento por eso 