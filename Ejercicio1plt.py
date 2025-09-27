import matplotlib.pyplot as plt

Meses=["Enero", "Febrero", "Marzo", "Abril"]
Ventas=[1500,1800,1200,2000]
Gasto_publicitario=[500,700,400,800]

#1.- Gráfico de barras

plt.plot(Meses,Ventas, marker="o")
plt.title("Evolución de ventas")
plt.xlabel("Meses")
plt.ylabel("Ventas")
plt.grid(True)
plt.show()