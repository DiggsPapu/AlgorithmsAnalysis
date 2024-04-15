# AlgorithmsAnalysis

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

## Problema 3
Siempre contendra el objeto con mayor relacion de costo por peso debido a que siempre sera el primer objeto en ingresar en la bolsa. Esto debido a que este objeto tiene la mejor relacion de ganancia por cada unidad de peso (Recordando el knapsack problem va jalando los objetos en virtud de cual tiene la maxima relacion v/w.) entonces siempre jalara ese objeto porque tiene la mejor y en el caso de no jalar ese objeto no se podria maximizar la ganancia G de manera que se obtendria una ganancia T < G.
## Problema 4

## Problema 5

## Problema 6