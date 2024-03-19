import numpy as np
import pandas as pd

#Genere un arreglo de 6 elementos de texto renombrando sus índices e imprima los datos
#Create a Serie
#languages = ["Python", "GO", "JavaScript", "Java", "SQL", "PHP"]
#position = [1, 2, 3, 4, 5, 6]
#languages_series = pd.Series(languages , index=position)
#print("Serie:")
#print(languages_series)

#Genere un arreglo de 3 elementos de texto con sus 3 valores numéricos e imprima los datos
#data2 = pd.Series({'Enero': 40000, 'Febrero': 30000, 'Marzo': 45000})
#print(data2)

#Genere un arreglo de 10 números aleatorios e imprima todos los números,
# los primeros 5 números, los últimos 5, los 2 primeros y los 2 últimos.
data3 = pd.Series(np.random.randn(10))
print(data3)
print(data3.head())
print(data3.tail())
print(data3.head(2))
print(data3.tail(2))










