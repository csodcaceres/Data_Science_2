# Has recibido una solicitud para generar números de token para acceder a la aplicación de una 
# empresa. 
# El token debe ser par y variar de 1000 a 9998. 
# Escribe un código que solicite el nombre de la persona usuaria y muestre un mensaje junto a este 
# token generado aleatoriamente

import random

nombre_usuario = input('Ingrese nombre de usuario: ')
token_generado = random.randrange(1000, 9998, 2)

print(f'Hola {nombre_usuario}, tu token de acceso es {token_generado} ¡Bienvenido/a!')
