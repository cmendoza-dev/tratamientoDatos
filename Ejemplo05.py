import numpy as np
import pandas as pd

data = pd.DataFrame(np.array([['Enero', 'Febrero', 'Marzo'],[25000, 45000, 40000],
                              [15000, 55000, 20000],
                              [5000, 4000, 7090]]))

data2 = pd.DataFrame(np.array([[25000, 45000, 40000],[15000, 55000, 20000],[5000, 4000, 7090]]))
print("Estadísticas del DataFrame: ")
print(data2.describe())
print("Media: ", data2.mean())
print("Correlación: ", data2.corr())
print("Más alto: ", data2.max())
print("Más bajo: ", data2.min())
print("Mediana: ", data2.median())
print("Desviación estándar: ", data2.std())
print("Primera columna: ", data2[0])
print("Dos columna: ", data2[[0, 1]])
print("Primera fila y última columna: ",)
print(data2.iloc[0][2])
print("Valores de la primera fila: ",)
print(data2.loc[0])

#print(data)
#print('Número de filas y columnas: ', data.shape)


