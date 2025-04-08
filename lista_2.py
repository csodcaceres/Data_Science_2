# Escribe una función que genere la tabla de multiplicar de un número entero del 1 al 10, 
# según la elección del usuario. Como ejemplo, para el número 7, 
# la tabla de multiplicar se debe mostrar en el siguiente formato:


def tablaMultiplicar(numero):
    print(f'Tabla de multiplicar del {numero}')

    for i in range(11):
        print(f'{numero} x {i} = {numero * i}')

tablaMultiplicar(7)