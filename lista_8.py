# Una posible solución a este punto la encuentras a continuación:

goles_marcados = [2, 1, 3, 1, 0]
goles_sufridos = [1, 2, 2, 1, 3]

def calcula_puntos(goles_marcados, goles_sufridos):
    puntos = 0

    for i in range(len(goles_marcados)):
        if goles_marcados[i] > goles_sufridos[i]:
            puntos += 3
        elif goles_marcados == goles_sufridos[i]:
            puntos += 1

    aprobado = 100 * puntos / (len(goles_marcados) * 3)
    return (puntos, aprobado)

puntos, aprobado = calcula_puntos(goles_marcados, goles_sufridos)
print(f'La puntuacion del equipo fue de {puntos} y su rendimiento fue de {round(aprobado)}%')
