# Data Science Funciones

# Pip y PyPI

El PIP es un administrador de paquetes para Python. A través de él, tenemos acceso a las bibliotecas ya instaladas en nuestra aplicación junto con la versión de cada una de ellas. Desde las líneas de comandos, podemos instalar, actualizar y eliminar paquetes de Python. Con pip, podemos instalar fácilmente paquetes de terceros en proyectos de Python.

Para acceder a todos los paquetes instalados en nuestro Jupyter Notebook en Colab, podemos escribir el siguiente código:

# Imprimir todos los paquetes instalados en el entorno y sus versiones
!pip list

pip funciona conectándose al Python Package Index (PyPI), que es el repositorio centralizado más grande para paquetes de Python con miles de bibliotecas disponibles para la instalación. Podemos buscar en PyPI para encontrar paquetes que satisfagan nuestras necesidades y luego usar pip para instalarlos en nuestros proyectos.

PyPI es mantenido por la Python Software Foundation y contiene una amplia variedad de paquetes de Python. En él, se publican paquetes de Python para que otros desarrolladores puedan usarlos. Por lo tanto, pip y PyPI son dos herramientas importantes en Python.

# Para saber más: otras formas de importación
Ya hemos trabajado con dos formas de importar paquetes: import nombre_biblioteca para todo el paquete y from nombre_biblioteca import metodo para solo un método de una biblioteca dada.

La importación de métodos específicos de una biblioteca puede tener algunas ventajas para nuestro proyecto, como:

Economía de memoria: cuando importamos una biblioteca completa, todo su código se carga en la memoria, incluso si no utilizamos todos sus métodos. Importar solo los métodos que necesitamos puede ahorrar memoria, especialmente en programas con grandes bibliotecas.

Mayor claridad en el código: importar solo los métodos que vamos a usar hace que el código sea más claro y fácil de entender.

Reducción de conflictos de nombres: al importar una biblioteca completa, podríamos tener conflictos de nombres con otras variables o funciones en nuestro código.

Reducción en el tiempo de ejecución: como no se importa toda la biblioteca, el tiempo de ejecución del programa puede ser más rápido, ya que se carga y se interpreta menos código en la memoria por el intérprete de Python.

Además de las formas vistas anteriormente, podemos mencionar dos ejemplos que podríamos encontrar en sus prácticas y estudios del lenguaje Python:

from nombre_biblioteca import met_1, met_2

Este código resulta en la importación de 2 o más métodos de una biblioteca, evitando repetir la importación cada vez que se desee un método. Por ejemplo, podríamos importar 2 métodos de la biblioteca random para tomar una muestra de 5 valores de una lista de 20 valores generada aleatoriamente con números del 0 al 99.

from random import randrange, sample

lista = []

for i in range(0, 20):
  lista.append(randrange(100))

sample(lista, 5)

Salida: [28, 66, 53, 81, 85]


----------------------------------------------------------------------------------------------

from nombre_biblioteca import *

Esta forma se utiliza para importar todos los métodos de una biblioteca dada. La diferencia con import nombre_biblioteca es que, en este caso, no necesitamos usar el nombre de la biblioteca para llamar a un método. Podemos pasar solo su nombre. Por ejemplo, si vamos a calcular la raíz cuadrada de un cierto número, podríamos seguir una de las dos formas:

Usando import nombre_biblioteca:

import math 

n = int(input("Digite um número positivo para calcular sua raiz quadrada:"))
print(f"\nA raiz quadrada de {n} é igual a {math.sqrt(n)}")

----------------------------------------------------------------------------------------------

Usando from nombre_biblioteca import *:

from math import * 

n = int(input("Digite um número positivo para calcular sua raiz quadrada:"))
print(f"\nA raiz quadrada de {n} é igual a {sqrt(n)}")


Observa que, en el segundo ejemplo, hemos omitido el nombre math utilizando el método deseado y escribiendo el código con menos caracteres.

Nota: La importación en este sentido requiere ciertos cuidados:

Podríamos tener conflictos de nombres entre las variables. Por ejemplo, si tenemos una función llamada sqrt antes de importar la de la biblioteca math.

Podríamos reducir la eficiencia de la ejecución si el número de funciones importadas es grande.

No queda explícito de dónde proviene esa variable, método o clase.

----------------------------------------------------------------------------------------------

Una empresa quiere calcular el número de artículos vendidos a partir de los ingresos de la venta y el valor unitario del producto. Además, necesita redondear hacia arriba la cantidad de artículos vendidos en caso de que el valor no sea un número entero.

Supongamos que los ingresos fueron de 1000 dolares y la unidad del producto se vende a 15 dolares. ¿Cuál son los códigos a continuación utiliza el método ceil de la biblioteca math para realizar este redondeo?

Puedes consultar la documentación del método ceil.

from math import cail

receta = 1000
unidades = 15

print(f'La empresa vendio aproximadamente {math.cail(receta/unidades)} unidades')

----------------------------------------------------------------------------------------------

otra opcion seria:

import math

receta = 1000
unidades = 15

print(f'La empresa vendio aproximadamente {math.cail(receta/unidades)} unidades')

----------------------------------------------------------------------------------------------

Vamos a practicar lo que hemos aprendido hasta ahora resolviendo los problemas propuestos en código.

Calentamiento

1 - Escribe un código para instalar la versión 3.7.1 de la biblioteca matplotlib.

2 - Escribe un código para importar la biblioteca numpy con el alias np.

3 - Crea un programa que lea la siguiente lista de números y elija uno al azar.

lista = [8, 12, 54, 23, 43, 1, 90, 87, 105, 77]

4 - Crea un programa que genere aleatoriamente un número entero menor que 100.

5 - Crea un programa que solicite a la persona usuaria ingresar dos números enteros y calcule la potencia del primer número elevado al segundo.

# Aplicando a proyectos

6 - Se debe escribir un programa para sortear a un seguidor de una red social para ganar un premio. La lista de participantes está numerada y debemos elegir aleatoriamente un número según la cantidad de participantes. Pide a la persona usuaria que proporcione el número de participantes del sorteo y devuelve el número sorteado.

7 - Has recibido una solicitud para generar números de token para acceder a la aplicación de una empresa. El token debe ser par y variar de 1000 a 9998. Escribe un código que solicite el nombre de la persona usuaria y muestre un mensaje junto a este token generado aleatoriamente

print(f"Hola, {nombre_usuario}, tu token de acceso es {token_generado} ¡Bienvenido/a!")

8 - Para diversificar y atraer nuevos clientes, una lanchonete creó un ítem misterioso en su menú llamado "ensalada de frutas sorpresa". En este ítem, se eligen aleatoriamente 3 frutas de una lista de 12 para componer la ensalada de frutas del cliente. Crea el código que realice esta selección aleatoria según la lista dada.

frutas = ["manzana", "banana", "uva", "pera", "mango", "coco", "sandia", "fresa", "naranja", "maracuya", "kiwi", "cereza"]

9 - Has recibido un desafío para calcular la raíz cuadrada de una lista de números, identificando cuáles resultan en un número entero. La lista es la siguiente:

numeros = [2, 8, 15, 23, 91, 112, 256]

10 - Haz un programa para una tienda que vende césped para jardines. Esta tienda trabaja con jardines circulares y el precio del metro cuadrado de césped es de R$ 25,00. Pide a la persona usuaria el radio del área circular y devuelve el valor en reales de cuánto tendrá que pagar.


Vamos a practicar lo que hemos aprendido hasta ahora resolviendo los problemas propuestos en código.

Calentamiento

1 - Escribe un código que lee la lista siguiente y realiza:

lista = [16, 14, 63, 65, 17, 99, 70, 11, 20, 48, 79, 32, 17, 89, 12, 25, 66]
# 1. Leer el tamaño de la lista
# 2. Leer el valor máximo y mínimo
# 3. Calcular la suma de los valores de la lista
# 4. Mostrar un mensaje al final: La lista tiene `tamano` números, donde el mayor 
# es `mayor` y el menor es `menor`. La suma de los valores es `suma`.


2 - Escribe una función que genere la tabla de multiplicar de un número entero del 1 al 10, según la elección del usuario. Como ejemplo, para el número 7, la tabla de multiplicar se debe mostrar en el siguiente formato:

# Tabla del  7:
# 7 x 0 = 0
# 7 x 1 = 7
# [...]
# 7 x 10 = 70


3 - Crea una función que lea la siguiente lista y devuelva una nueva lista con los múltiplos de 3:

[97, 80, 94, 88, 80, 1, 16, 53, 62, 32, 24, 99]


4 - Crea una lista de los cuadrados de los números de la siguiente lista [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]. Recuerda utilizar las funciones lambda y map() para calcular el cuadrado de cada elemento de la lista.

Aplicando a proyectos

5 - Has sido contratado como científico(a) de datos de una asociación de skate. Para analizar las notas recibidas por los skaters en algunas competiciones a lo largo del año, necesitas crear un código que calcule la puntuación de los atletas. Para ello, tu código debe recibir 5 notas ingresadas por los jueces.

6 - Para cumplir con una demanda de una institución educativa para el análisis del rendimiento de sus estudiantes, necesitas crear una función que reciba una lista de 4 notas y devuelva:

# mayor nota
# menor nota
# media
# situación (Aprobado(a) o Reprobado(a))
# Uso de la función
# Mostrar: El estudiante obtuvo una media de `media`, con la mayor nota de `mayor` puntos y la menor nota de `menor` puntos y fue `situacion`.)


7 - Has recibido una demanda para tratar 2 listas con los nombres y apellidos de cada estudiante concatenándolos para presentar sus nombres completos en la forma Nombre Apellido. Las listas son:

nombres = ["juan", "MaRia", "JOSÉ"]
apellidos = ["SILVA", "sosa", "Tavares"]

# Normalizar nombres y apellidos y crear una nueva lista con los nombres completos
# Puedes apoyarte en la función map()


8 - Como científico de datos en un equipo de fútbol, necesitas implementar nuevas formas de recopilación de datos sobre el rendimiento de los jugadores y del equipo en su conjunto. Tu primera acción es crear una forma de calcular la puntuación del equipo en el campeonato nacional a partir de los datos de goles marcados y recibidos en cada juego.

Escribe una función llamada calcula_puntos() que recibe como parámetros dos listas de números enteros, representando los goles marcados y recibidos por el equipo en cada partido del campeonato. La función debe devolver la puntuación del equipo y el rendimiento en porcentaje, teniendo en cuenta que la victoria vale 3 puntos, el empate 1 punto y la derrota 0 puntos.

Nota: si la cantidad de goles marcados en un partido es mayor que los recibidos, el equipo ganó. En caso de ser igual, el equipo empató, y si es menor, el equipo perdió. Para calcular el rendimiento, debemos hacer la razón entre la puntuación del equipo y la puntuación máxima que podría recibir.

Para la prueba, utiliza las siguientes listas de goles marcados y recibidos:

goles_marcados = [2, 1, 3, 1, 0]
goles_recibidos = [1, 2, 2, 1, 3]
# Texto probablemente mostrado:
# La puntuación del equipo fue `puntos` y su rendimiento fue `desempeno`%"


9 - Te han desafiado a crear un código que calcule los gastos de un viaje a una de las cuatro ciudades desde Recife, siendo ellas: Salvador, Fortaleza, Natal y Aracaju.

El costo diario del hotel es de 150 reales en todas ellas y el consumo de gasolina en el viaje en coche es de 14 km/l, siendo que el precio de la gasolina es de 5 reales por litro. Los gastos con paseos y alimentación a realizar en cada una de ellas por día serían [200, 400, 250, 300], respectivamente.

Sabiendo que las distancias entre Recife y cada una de las ciudades son aproximadamente [850, 800, 300, 550] km, crea tres funciones: la primera función calcula los gastos de hotel (gasto_hotel), la segunda calcula los gastos de gasolina (gasto_gasolina) y la tercera los gastos de paseo y alimentación (gasto_paseo).

Para probar, simula un viaje de 3 días a Salvador desde Recife. Considera el viaje de ida y vuelta en coche.

# Texto probablemente mostrado:
# Con base en los gastos definidos, un viaje de [dias] días a [ciudad] desde 
# Recife costaría [gastos] reales.


10 - Has comenzado una pasantía en una empresa que trabaja con procesamiento de lenguaje natural (NLP). Tu líder te solicitó que crees un fragmento de código que reciba una frase escrita por el usuario y filtre solo las palabras con un tamaño mayor o igual a 5, mostrándolas en una lista. Esta demanda se centra en el análisis del patrón de comportamiento de las personas al escribir palabras de esta cantidad de caracteres o más.

Consejo: utiliza las funciones lambda y filter() para filtrar estas palabras. Recordando que la función integrada filter() recibe una función (en nuestro caso, una función lambda) y filtra un iterable según la función. Para tratar la frase, utiliza replace() para cambiar ',' '.', '!' y '?' por espacio.


