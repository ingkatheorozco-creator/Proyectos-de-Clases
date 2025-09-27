import matplotlib.pyplot as plt

edades=(20,21,22,25,25,26,27,30,35,40)

plt.hist(edades,bins=5, color="green", edgecolor="white")
plt.title("Distribución de Edades")
plt.xlabel("Rango de Edades")
plt.ylabel("Frecuencia")
plt.show()