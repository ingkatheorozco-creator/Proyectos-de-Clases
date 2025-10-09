import pandas as pd

df= pd.read_csv("SAN BLAS.csv")
#print(df)

#df= df.drop(columns= ["CEDULA", "1ER_NOM", "2DO_NOM","1ER_APE", "NUMERO_FACTURA", "NOM_CENTRO"])
#print (df)

#df= df.drop(columns= ["2DO_APE", "FECHA_NAC", "COD_HIS","COD_DX", "COD_CENTRO", "NOM_HIS", "#_FOLIO", "MEDICO", "VIA_INGRESO", "SERVICIO", "C_EXT", "F_CON", "MES" ])
#print(df)

print(df.columns)

df_limpio=df.iloc[:,[6,12,13,14,15,18,21,22]]
print(df_limpio)

print(df_limpio.columns)

df_limpio.to_csv('datos_limpios.csv', index=False)

print("Archivo limpio guardado.csv")