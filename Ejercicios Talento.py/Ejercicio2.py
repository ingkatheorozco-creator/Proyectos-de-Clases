import pandas as pd

def analizador_ventas(url):

    df=pd.read_csv(url, decimal=",")
    print("1.Datos cargados")
    print(df)
    df["Cantidad"]=[2,4,5,6,7,20,12,15,16,2,3,5,6,9,10,15,12,8,9,0]
    print(df)
    df["Ventas"]=df['PrecioUnitario']*df['Cantidad']
    print(df)
    VentasCategoria = df.groupby('Categoría')['Ventas'].sum()
    print(VentasCategoria)
    df['TotalVentasCategoria'] = df['Categoría'].map(VentasCategoria)

# Paso Ordenar primero por TotalVentasCategoria (mayor a menor), luego por Ventas (mayor a menor)
    df_ordenado = df.sort_values(by=['TotalVentasCategoria', 'Ventas'], ascending=[False, False])

# Paso (Opcional) Eliminar columna auxiliar
    df_ordenado = df_ordenado.drop(columns='TotalVentasCategoria')

# Mostrar resultado
    print(df_ordenado)


url="https://docs.google.com/spreadsheets/d/18LQO7KKhV8kQ_rxegxFDAcscKxs5Drii/export?format=csv"
analizador_ventas(url)