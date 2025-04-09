# Ahora, necesitamos utilizar los promedios calculados en el ejemplo anterior, y agruparlos 
# con el nombre de los respectivos estudiantes. 
# Esto será necesario para generar una lista que seleccione a aquellos estudiantes que posean 
# un promedio final mayor o igual a 8 para concursar por una beca de estudios para el 
# próximo año lectivo. Los datos recibidos corresponden a una lista de tuplas con los nombres 
# y los códigos de los estudiantes junto a la lista de promedios calculados previamente.

# Nota: El número de código será diferente cada vez que se ejecute la celda que los genera, 
# por lo tanto, es completamente normal que estos códigos sean diferentes.

# Lista de nombres con matriculo
nombres = [('Juan', 'J664'), ('Maria', 'M444'), ('José', 'J738'), ('Claudia', 'C867'), ('Ana', 'A559')]

# Lista de promedios
promedio = [9.0, 7.3, 5.8, 6.7, 8.5]

# Vamos a tomar solo los nombres de nuestra lista nombres
nombres = [nombre[0] for nombre in nombres]

#  Para lograr parear los promedios y los nombres fácilmente, podemos acudir a otra 
# built-in function: zip()

# Esta recibe uno o más iterables (lista, string, dict, etc.) y los retorna como un iterador 
# de tuplas donde cada elemento de los iterables es pareado.

estudiantes = list(zip(nombres, promedio))

candidatos = [estudiante[0] for estudiante in estudiantes if estudiante[1] >= 8]
print(candidatos)

