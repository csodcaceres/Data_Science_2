# Crea una función que lea la siguiente lista y devuelva una nueva lista con los múltiplos de 3:
# lista_original = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

def multiplosDeTres(lista):
    return [num for num in lista if num % 3 == 0]

# Uso de la funcion
lista_original = [97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]

multiplo_tres = multiplosDeTres(lista_original)
print(multiplo_tres)
