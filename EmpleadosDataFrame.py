import pandas as pd

# Create a DataFrame from a dictionary
#Genere un arreglo de 6 elementos de texto con sus respectivos valores numéricos e imprima los datos.
ventas = {'Meses ': ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"], 'Monto':[25000,45000,40000,38000,75000,50000]}
data = pd.DataFrame(ventas)
#print(data)

#atributos = campo
ventas = {'Meses': ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"], 'Monto':[25000,45000,40000,38000,75000,50000]}
data = pd.DataFrame(ventas, columns=["Monto", "Meses"])
print(data)

