import matplotlib.pyplot as plt

productos = ["Manzanas", "Peras", "Naranjas"]
ventas= [50,80,40]

plt.bar(productos,ventas)
plt.title("Ventas por Producto")
plt.xlabel("Productos")
plt.ylabel("Ventas")
plt.show()