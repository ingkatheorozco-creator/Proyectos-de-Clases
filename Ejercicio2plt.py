import matplotlib.pyplot as plt

edades = [22,25,30,30,32,35,40,42,50,55,60,60,65,70,75]

#Histograma
#Ajusta el numero de bins
#Asegurate incluir titulo, nombres ejes, y colores

plt.hist(edades,bins=10, color="green", edgecolor="white")
plt.title("Distribución de Edades")
plt.xlabel("Rango de Edades")
plt.ylabel("Frecuencia")
plt.show()