# Para cumplir con una demanda de una institución educativa para el análisis del rendimiento 
# de sus estudiantes, necesitas crear una función que reciba una lista de 4 notas y devuelva:

def analisis_notas(notas):
    mayor = max(notas)
    menor = min(notas)
    media = sum(notas) / len(notas)
    situacion = 'Aprobado' if media >= 6 else 'Reprobado'

    return mayor, menor, media, situacion

# Uso de la funcion
notas_estudiantes = [float(input(f'Ingrese la nota {i + 1}: ')) for i in range(4)]
resultado = analisis_notas(notas_estudiantes)

print(f'El estudiante obtuvo una media de {resultado[2]:.2f}, con la mayor nota de {resultado[0]:.2f} puntos y la menor nota de {resultado[1]:.2f} puntos y fue {resultado[3]}')
