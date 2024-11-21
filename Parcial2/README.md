# AlgorithmsAnalysis
El video con las explicaciones y la ejecución del problema 1 y el problema 2 sería este:https://youtu.be/f6P9QZFP1U4
Así mismo, está el pdf con las explicaciones de los tiempos de los dos problemas.
## Problema 1

* Explique porque este problema exhibe subestructura optima.
Se puede obtener que la subestructura óptima para una combinación de longitud n, sería agarrar combinaciones de longitud n-1 y agregarle números adyacentes, obteniendo las combinaciones de manera fácil y rápida.
* Explique una idea o solucion que exhiba subproblemas traslapados e indique como los mismos problemas se computan repetidamente.
La idea es que le pase un dígito y resuelva las combinaciones para este dígito, de manera que inserte este dígito y después desarrolle todos los caminos adyacentes para este dígito. Sin embargo, todo lo que está después de este dígito podría ser otro camino para otro dígito, de manera que se obtiene un problema traslapado, por ejemplo "5252525252" para el dígito 5 puede también ser para 2 dado "2252525252", repitiendo el procedimiento y obteniendo un problema traslapado.
* Encuentre el tiempo de complejidad para este algoritmo.
* Usando su programa, encuentre las combinaciones totales posibles para n = 10.
1806282
El github gist es:https://gist.github.com/DiggsPapu/bcc1bf76718af7ce999a4e8bca77f714
## Problema 2
El github gist es:https://gist.github.com/DiggsPapu/eb9e66f6601ee410ed5a8006ed5be201
## Problema 3
Siempre contendra el objeto con mayor relacion de costo por peso debido a que siempre sera el primer objeto en ingresar en la bolsa. Esto debido a que este objeto tiene la mejor relacion de ganancia por cada unidad de peso (Recordando el knapsack problem va jalando los objetos en virtud de cual tiene la maxima relacion v/w.) entonces siempre jalara ese objeto porque tiene la mejor y en el caso de no jalar ese objeto no se podria maximizar la ganancia G de manera que se obtendria una ganancia T < G.

## Problema 5
Primero que nada, la independencia lineal es que un vector no se puede expresar como la operación de otros vectores.
Por lo tanto para demostrar que es una matroide se deben de demostrar tres propiedades:
* No vacío: el conjunto vacío no tiene columnas y es linealmente independiente, por lo que está en I.
* Hereditario: Supongamos que un conjunto de columnas A es linealmente independiente, y B es un subconjunto de este conjunto, ambos son linealmente independientes. ¿Por qué? Porque en caso de que si se combinara de alguna forma las columnas de B resultando en un vector 0, en A realizando lo mismo debería de dar 0, sin embargo, esto generaría una contradicción de la independencia lineal de A.
* Independencia de intercambio: Suponiendo que A y B son subconjuntos de columnas en I, pero A tiene más columnas que B. Dado que A tiene más, hay una columna que no está en B, agregandola hay que verificar si aún es linealmente independiente. En caso de que no lo sea, esto sería una contradicción porque en primer lugar A no sería independiente.
