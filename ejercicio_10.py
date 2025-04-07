# Haz un programa para una tienda que vende césped para jardines. 
# Esta tienda trabaja con jardines circulares y el precio del metro cuadrado de césped es de $ 25,00.
# Pide a la persona usuaria el radio del área circular y devuelve el valor en pesos de cuánto 
# tendrá que pagar.

import math

precio_metro_cuadrado = 25.00
radio = float(input('Ingrese el radio del area circular en metros: '))
area = math.pi * math.pow(radio, 2)
costo_total = precio_metro_cuadrado * area

print(f'El costo total es de $ {round(costo_total)}')
