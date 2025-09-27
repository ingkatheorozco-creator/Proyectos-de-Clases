import matplotlib.pyplot as plt

Ingresos=[100,200,300,400,500]
Gastos=[20,40,60,80,100]

plt.scatter(Gastos, Ingresos, color="red")
plt.title("Relación entre Gasto e Ingresos")
plt.xlabel("Gastos Publicitarios")
plt.ylabel("Ingresos")
plt.show()