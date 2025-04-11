# Andrés recibió una solicitud para analizar el conjunto de datos que contiene información sobre la 
# altura y el peso de varias personas. 
# Para procesar estos datos, André utilizó la estructura de list comprehension para calcular y 
# también guardar los datos del Índice de Masa Corporal (IMC). 

### El código genera una lista con los IMCs de cada persona en el conjunto de datos. 


alturas = [1.70, 1.80, 1.65, 1.75, 1.90]
pesos = [65, 80, 58, 70, 95]

imc = [round((peso / altura**2), 1) for altura, peso in zip(alturas, pesos)]
print(imc)
