import matplotlib.pyplot as plt

meses= ["Enero", "Febrero", "Marzo"]
ventas=[200,250,300]

plt.plot(meses,ventas, marker="o")
plt.title("Evolución de ventas")
plt.xlabel("Meses")
plt.ylabel("Ventas")
plt.grid(True)
plt.show()

