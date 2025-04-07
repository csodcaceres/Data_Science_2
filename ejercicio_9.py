# Has recibido un desafío para calcular la raíz cuadrada de una lista de números, 
# identificando cuáles resultan en un número entero. 
# La lista es la siguiente:

import math
numeros = [2, 8, 15, 23, 91, 112, 256, 512, 1024]

raices_enteras = [num for num in numeros if math.sqrt(num) % 1 == 0]
print(f'Numeros con raices enteras: {raices_enteras}')

