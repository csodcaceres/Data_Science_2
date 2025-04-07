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

