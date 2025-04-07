# Crea un programa que solicite a la persona usuaria ingresar dos números enteros y 
# calcule la potencia del primer número elevado al segundo.

import math

num1 = int(input('Ingrese el primer numero: '))
num2 = int(input('Ingrese el segundo numero: '))

resultado = math.pow(num1, num2)
print(resultado)
