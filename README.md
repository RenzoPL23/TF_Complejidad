## TPComplejidad
### Tales Salesman Problem
#### Introducción
El problema del vendedor viajero responde a la siguiente pregunta: dada una lista de ciudades y las distancias entre cada par de ellas. 

¿Cuál es la ruta más corta posible que visita cada ciudad exactamente una vez y al finalizar regresa a la ciudad origen? Este es un problema  

NP-Hard(conjunto de los problemas de decisión) dentro en la optimización combinatoria.   
El problema fue formulado por primera vez en 1930 y la motivación que encontramos en el problema es que es uno de los problemas de optimización más estudiados. Es usado como prueba para muchos métodos de optimización.Aunque el problema es computacionalmente complejo, una gran cantidad de heurísticas y métodos exactos son conocidos, de manera que, algunas instancias desde cien hasta miles de ciudades pueden ser resueltas.
Encontrar una solución con los conocimientos adquiridos hasta el momento en el curso de complejidad algorítmica es un reto para los alumnos, y ayudara a desarrollar nuestro pensamiento crítico al momento de solucionar problemas
#### Objetivos
- Encontrar la mayor cantidad de conexiones con las mínimas distancias de un nodo 'x' a un nodo 'y' en un tiempo optimo para las 8 bases de datos. 
- Encontrar distintos tipos de algoritmos usando los temas visto en la segunda parte del curso de Complejidad Algoritmica: Kruscal, Prim, Programación Dinámica, Bellman-Ford Floyd-Warshall, Johnson o Algoritmos Greedy. 
- Desarrollar algoritmos que nos permitan encontrar una solucion (no necesariamente la mas optima) de las 8 bases de datos con las que se trabaja. 
- Demostrar que las propuestas presentadas son escalables con respecto a la cantidad de datos con los que se trabaje.
#### Marco teorico
Algoritmo 1:
- BellmanFord: «El algoritmo de Bellman-Ford (algoritmo de Bell-End-Ford) produce el camino más corto en un grafo dirigido ponderado (en el que el peso de ciertas aristas puede ser negativo). Con lo que el AlgoritmoBellman-Ford en general se emplea cuando hay aristas con peso negativo. Este algoritmo fue desarrollado por Richard Bellman, Samuel End y Lester Ford.» (Paraisodigital.org, 2018)
- Algoritmo Greedy:»El propósito de un algoritmo voraz es encontrar una solución, es decir, una asociación de valores a todas las variables tal que el valor de la función objetivo sea óptimo. Para ello sigue un proceso secuencial en el que a cada paso toma una decisión (decide qué valor del dominio le ha de asignar a la variable actual) aplicando siempre el mismo criterio (función de selección). La decisión es localmente óptima, es decir, ningún otro valor de los disponibles para esa variable lograría que la función objetivo tuviera un valor mejor, y luego comprueba si la puede incorporar a la secuencia de decisiones que ha tomado hasta el momento, es decir, comprueba que la nueva decisión junto con todas las tomadas anteriormente no violan las restricciones y así consigue una nueva secuencia de decisiones factible.» (Universidad Politecnica de Cataluño, 2008)

El algoritmo consiste en tomar 2 de las de los nodos que esten lo mas lejos posible, y estableciendo uno como inicial. Luego utilizando BellmanFord se encuentra la ruta mas efectiva del nodo inicial hasta su nodo mas lejano. Una vez trasada esta ruta se usa un algoritmo greedy partiendo del nodo mas alejado del inicial antes establecido, este va escogiendo su siguiente coneccion que este lo mas cerca al nodo antes especificado hasta que encuentre el nodo inicial. En caso que el algoritmo greddy encuentre una situacion en la que no puede continuar porque sus conecciones han sido todas ya visitadas este usara backtracking para encontrar otra ruta posible.  
Algoritmo 2:  
- Prim: El algoritmo incrementa continuamente el tamaño de un árbol, comenzando por un vértice inicial al que se le van agregando sucesivamente vértices cuya distancia a los anteriores es mínima. Esto significa que en cada paso, las aristas a considerar son aquellas que inciden en vértices que ya pertenecen al árbol.  
El árbol recubridor mínimo está completamente construido cuando no quedan más vértices por agregar.  
El algoritmo podría ser informalmente descrito siguiendo los siguientes pasos:
- Inicializar un árbol con un único vértice, elegido arbitrariamente del grafo.
- Aumentar el árbol por un lado. Llamamos lado a la unión entre dos vértices: de las posibles uniones que pueden conectar el árbol a los vértices que no están aún en el árbol, encontrar el lado de menor distancia y unirlo al árbol.
- Repetir el paso 2 (hasta que todos los vértices pertenezcan al árbol)

Algoritmo 3:  
- Held–Karp:
Calcula las soluciones de todos los subproblemas comenzando con los más pequeños. Siempre que la computación de una solución requiera soluciones para problemas más pequeños utilizando las ecuaciones recursivas anteriores, busque estas soluciones que ya están computadas. Para calcular un recorrido de distancia mínima, use la ecuación final para generar el primer nodo y repita para los otros nodos. Para este problema, no podemos saber qué subproblemas necesitamos resolver, por lo que los resolvemos todos.
#### Tiempo asintótico
Algoritmo 1:  
BellmanFord:  
T(n)=n x n  
Greedy:  
- En el mejor de los casos:
T(n)=n
- En el peor de los casos:
T(n)=n x n

Por lo tanto el algoritmo creado tendra un tiempo maximo de:
T(n)=(n x n)+(n x n)

Algoritmo 2:  
Prim:
- T(n) ∈ Θ(n^2)  
Algoritmo 3:
- Para cualquier vértice s, la duración del recorrido óptimo del vendedor viajero es L (s, V ∖ {s}, s). Debido a que el primer parámetro s es constante en todas las llamadas recursivas, hay Θ ((2^n)*n) subproblemas diferentes, y cada subproblema depende de un máximo de n otros. Por lo tanto, el algoritmo de programación dinámica se ejecuta en tiempo O ((2^n)*(n^2)).

#### Conclusiones 
Utilizar Bellmand Ford es una opcion factible para para encontrar una ruta entre x a y, sin embargo como no se tienen rutas negativas entonces no es necesario y un algoritmo como UCS puede ser mucho mas eficiente en cuanto al tiempo asindotico.
Hay algortmos que pueden servir para crear algoritmos que encuentren una buena solucion, como algoritmos que encuentran rutas mas cortas, programacion dinamica para reducir el tiempo, algoritmos greedy dependiendo como sean los datos, sin embargo no se tiene un algoritmo que por si solo pueda dar una solucion, siempre tiene que cambiarse varias partes del mismo o fucionarlos. Ademas los tiempos son muy grandes y no encuentran la mejor solucion solo una buena solucion.
Utilizando las diferentes bases de datos propuestas se puede notar como mientras mas grande es la base de datos (mas grande es el tiempo de ejecucion del problema. Esto se debe a que los algoritmos usados suelen tener un tiempo asindotico exponencial lo cual no es nada conveniente.

