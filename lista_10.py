# Una posible solución a este punto la encuentras a continuación:

# Solicitando una frase y separándola por espacios. Usando replace para cambiar
# puntuaciones por espacios.
frase = input("Escribe una frase: ")
frase = frase.replace(',',' ').replace('.',' ').replace('!',' ').replace('?',' ').split()

# Filtrando la frase en formato de lista, pasando a la lista tamaño
# solo las palabras con 5 o más caracteres e imprimiéndola en pantalla
tamano = list(filter(lambda x: len(x) >= 5, frase))
print(tamano)
