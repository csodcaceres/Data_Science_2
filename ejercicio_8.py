# Para diversificar y atraer nuevos clientes, una lanchonete creó un ítem misterioso en su menú 
# llamado "ensalada de frutas sorpresa". 
# En este ítem, se eligen aleatoriamente 3 frutas de una lista de 12 para componer la ensalada 
# de frutas del cliente. 
# Crea el código que realice esta selección aleatoria según la lista dada.

import random

frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", 
          "maracuya", "kiwi", "cereza"]

seleccion_frutas = random.sample(frutas, 3)
print(f'Ensalada de fruta sorpresa: {seleccion_frutas}')
