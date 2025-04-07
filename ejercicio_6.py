# Se debe escribir un programa para sortear a un seguidor de una red social para ganar un premio. 
# La lista de participantes está numerada y debemos elegir aleatoriamente un número según la 
# cantidad de participantes. 
# Pide a la persona usuaria que proporcione el número de participantes del sorteo y devuelve el 
# número sorteado.

import random

cantidad_participantes = int(input('Ingrese la cantidad de participantes: '))
numero_sorteado = random.randint(1,cantidad_participantes)
print(f'El numero sorteado es {numero_sorteado}')
