
import pandas as pd

# Lea el archivo de Excel Ventas02.xlsx ignorando la primera fila (encabezado)
# e imprima los datos.
archivo = pd.read_excel('Ventas02.xlsx', header=None, skiprows=1)
data=pd.DataFrame(archivo)
print(data)

