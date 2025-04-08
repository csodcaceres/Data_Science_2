# Has recibido una demanda para tratar 2 listas con los nombres y apellidos de cada estudiante 
# concatenándolos para presentar sus nombres completos en la forma Nombre Apellido. 
# Las listas son:

nombres = ["juan", "MaRia", "JOSÉ"]
sobrenombres = ["SILVA", "sosa", "Tavares"]

# Normalizar nombres y apellidos y crear una nueva lista con los nombres completos

nombre_normalizado = map(lambda x: x.capitalize(), nombres)
sobrenombres_normalizados = map( lambda x: x.capitalize(), sobrenombres)

nombres_completos = list(map(lambda x, y: f'Nombre completo: {x} {y}', nombre_normalizado, sobrenombres_normalizados))
print(nombres_completos)