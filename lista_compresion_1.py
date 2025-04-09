# Recibimos la demanda de crear una lista con el promedio de los estudiantes de la lista de listas 
# que creamos en la Situación 6, redondeando el promedio a una casilla decimal. 
# Recordando que cada lista de la lista de listas contiene las tres notas de cada estudiante.

def promedio(lista: list=[0]) -> float:
  ''' Función para calcular el promedio de notas en una lista

  lista: list, default [0]
    Lista con las notas para calcular el promedio
  return = calculo: float
    Promedio calculado
  '''

  calculo = sum(lista) / len(lista)

  return calculo

notas = [[8.0, 9.0, 10.0], [9.0, 7.0, 6.0], [3.4, 7.0, 7.0], [5.5, 6.6, 8.0], [6.0, 10.0, 9.5]]

promedios = [round(promedio(nota), 1) for nota in notas]
print(promedios)
