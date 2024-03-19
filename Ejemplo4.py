import pandas as pd

#Empleando DataFrame: Genere 2 arreglos de 6 elementos de texto con sus respectivos
# valores numéricos e imprima los datos, agregue el arreglo 2 sobre el arreglo 1 e imprima los datos.
ventas1 = {'Meses ': ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
          'Monto': [25000, 45000, 40000, 38000, 75000, 50000]}

ventas2 = {'Meses ': ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio"],
          'Monto': [10000, 15000, 19000, 32000, 53000, 40000]}

data1 = pd.DataFrame(ventas1)
data2 = pd.DataFrame(ventas2)
datos = data1.add(data2)

print(data1)
print(data2)
print(datos)


