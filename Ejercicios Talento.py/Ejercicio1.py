import pandas as pd

def analizador_ventas(url):

    df=pd.read_csv(url, decimal=",")
    print("1.Datos cargados")
    print(df)
    print("2.Las primeras 10 filas")
    print(df.head(10))
    print("3.Información del Dataframe")
    print("Número de Filas", df.shape[0])
    print("Número de columnas", df.shape[1])
    df.info()
    valor_nulos=df.isnull().sum()
    print("Valores nulos", valor_nulos)

url="https://docs.google.com/spreadsheets/d/18LQO7KKhV8kQ_rxegxFDAcscKxs5Drii/export?format=csv"
analizador_ventas(url)
