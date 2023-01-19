# Examen_Ordinario_EDA2_Carlota_S-nchez
El link a mi repositorio es: https://github.com/crltsnch/Examen_Ordinario_EDA2_Carlota_S-nchez.git

***EJERCICIO 1***

Ejercicio:
```
class Stormtroopers:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print('Creado con éxito')
    def clasificacion(self):
        codigoLegion = self.nombre.split("-")[0]
        print('Codigo Legion: ' + codigoLegion)
        print('Identificador de Cohoerte: ' + self.nombre.split("-")[1][0])
        print('Identificador de Siglo: ' + self.nombre.split("-")[1][1])
        print('Identificador de Escuadra: ' + self.nombre.split("-")[1][2])
        print('Numero de Trooper: ' + self.nombre.split("-")[1][3])

lista = [Stormtroopers('AK-3654', 7), Stormtroopers('LF-2564', 7), Stormtroopers('TK-8154', 7), Stormtroopers('TL-8654', 7)]
for stormtrooper in lista:
    stormtrooper.clasificacion()
 ```
 Main:
 
 ```
 from ej1 import *

if __name__ == '__main__':
    stormtrooper = Stormtroopers('AK-3654', 7)
    print(stormtrooper.nombre)
    print(stormtrooper.rango)
    stormtrooper.clasificacion()
    print(stormtrooper.nombre.split("-")[0])
    print(stormtrooper.nombre.split("-")[1][0])
    print(stormtrooper.nombre.split("-")[1][1])
    print(stormtrooper.nombre.split("-")[1][2])
    print(stormtrooper.nombre.split("-")[1][3])
```

Test:
```
import pytest
from ej1 import Stormtroopers

def test_stormtrooper():
    stormtrooper = Stormtroopers('AK-3654', 7)
    assert stormtrooper.nombre == 'AK-3654'
    assert stormtrooper.rango == 7
    stormtrooper.clasificacion()
    assert stormtrooper.nombre.split("-")[0] == "AK"
    assert stormtrooper.nombre.split("-")[1][0] == "3"
    assert stormtrooper.nombre.split("-")[1][1] == "6"
    assert stormtrooper.nombre.split("-")[1][2] == "5"
    assert stormtrooper.nombre.split("-")[1][3] == "4"
```
 ***EJERCICIO 2***
 
 Ejercicio:
 ```
 class Stormtroopers:
    def __init__(self, nombre, rango):
        self.nombre = nombre
        self.rango = rango
        print('Creado con éxito')
    def clasificacion(self):
        codigoLegion = self.nombre.split("-")[0]
        print('Codigo Legion: ' + codigoLegion)
        print('Identificador de Cohoerte: ' + self.nombre.split("-")[1][0])
        print('Identificador de Siglo: ' + self.nombre.split("-")[1][1])
        print('Identificador de Escuadra: ' + self.nombre.split("-")[1][2])
        print('Numero de Trooper: ' + self.nombre.split("-")[1][3])
    def __str__(self):
        return "Nombre: " + self.nombre + " Rango: " + str(self.rango)


lista = [Stormtroopers('AK-3654', 7), Stormtroopers('LF-2564', 7), Stormtroopers('TK-8154', 7), Stormtroopers('TL-8654', 7)]
for stormtrooper in lista:
    stormtrooper.clasificacion()
```
Main:
```
from ej2 import *

if __name__ == '__main__':
    # Creo un objeto de la clase Ej2
    ej2 = stormtrooper()
    # Ejecuto el método de la clase Ej2
    ej2.__str__()
```
Test:
```
import pytest
from ej2 import Stormtroopers

def test_stormtrooper():
    stormtrooper = Stormtroopers('AK-3654', 7)
    assert stormtrooper.nombre == 'AK-3654'
    assert stormtrooper.rango == 7
    stormtrooper.clasificacion()
    assert stormtrooper.nombre.split("-")[0] == "AK"
    assert stormtrooper.nombre.split("-")[1][0] == "3"
    assert stormtrooper.nombre.split("-")[1][1] == "6"
    assert stormtrooper.nombre.split("-")[1][2] == "5"
    assert stormtrooper.nombre.split("-")[1][3] == "4"

def test_stormtrooper_str():
    stormtrooper = Stormtroopers('AK-3654', 7)
    assert str(stormtrooper) == 'AK-3654 es un Stormtrooper de rango 7'
```
***EJERCICIO 3***

Ejercicio:

```
from datetime import datetime
class ArtefactosValiosos:
    def __init__(self, nombre, peso, precio, fechaCaducidad):
        self.nombre = nombre
        self.peso = peso
        self.precio = precio
        self.fechaCaducidad = fechaCaducidad
        print('Se ha creado un artefacto valioso')
    def __str__(self):
        return 'Nombre: ' + self.nombre + ' Peso: ' + str(self.peso) + ' Precio: ' + str(self.precio) + ' Fecha de caducidad: ' + str(self.fechaCaducidad)

def sortByDate(elem):
    return datetime.strptime(elem.fechaCaducidad, '%m/%d/%Y')

def main():
    lista = [ArtefactosValiosos('Diamante', 50, 500, '08/31/2024'),
    ArtefactosValiosos('Esmeralda', 50, 500, '07/28/2023'),
    ArtefactosValiosos('Perla', 50, 500, '09/30/2025')]
    lista.sort(key=sortByDate)
    for stormtrooper in lista:
        print(stormtrooper)

    print('Precio cambiado')
    lista[0].precio = 400
    print(lista[0]) 
```
Main:
```
from ej3 import *
if __name__ == '__main__':
    main()
```
Test:
```
from datetime import datetime
from ej3 import *

def test_ArtefactosValiosos_init():
    artefasto = ArtefactosValiosos('Diamante', 50, 500, '08/31/2024')
    assert artefasto.nombre == 'Diamante'
    assert artefasto.peso == 50
    assert artefasto.precio == 500
    assert artefasto.fechaCaducidad == '08/31/2024'

def test_ArtefactosValiosos_str():
    artefacto = ArtefactosValiosos('Diamante', 50, 500, '08/31/2024')
    assert str(artefacto) == 'Nombre: Diamante Peso: 50 Precio: 500 Fecha de caducidad: 08/31/2024'

def test_sortByDate():
    lista = [ArtefactosValiosos('Diamante', 50, 500, '08/31/2024'),
ArtefactosValiosos('Esmeralda', 50, 500, '07/28/2023'),
ArtefactosValiosos('Perla', 50, 500, '09/30/2025')]
    lista.sort(key=sortByDate)
    assert lista[0].nombre == 'Esmeralda'
    assert lista[1].nombre == 'Diamante'
```

***EJERCICIO 4***

Ejercicio:
```
class ArtefactosValiosos:
    def __init__(self, nombre, peso, precio, fechaCaducidad):
        self.nombre = nombre
        self.peso = peso
        self.precio = precio
        self.fechaCaducidad = fechaCaducidad
        print('Se ha creado un artefacto valioso')
    def __str__(self):
        return 'Nombre: ' + self.nombre + ' Peso: ' + str(self.peso) + ' Precio: ' + str(self.precio) + ' Fecha de caducidad: ' + str(self.fechaCaducidad)
    
def usarFuerza(mochila, numObjetos):
    if(len(mochila)>0):
        if mochila[len(mochila)-1].nombre == "Sable de Luz":
            print("Se han sacado " + str(numObjetos) + " objetos de la mochila")
        else:
            mochila.pop()
            usarFuerza(mochila, numObjetos+1)
    else:
        print("No hay objetos en la mochila")

def main():
    numObjetos = 0
    mochiila = [ArtefactosValiosos('Linterna', 500, 20, '05/28/2022'),
    ArtefactosValiosos('Sable de Luz', 500, 20, '05/28/2022'),
    ArtefactosValiosos('Esmeralda', 500, 20, '05/28/2022'), ArtefactosValiosos('Diamante', 500, 20, '05/28/2022')]
    usarFuerza(mochiila, numObjetos)
```
Main:
```
from ej4 import *

if __name__ == '__main__':
    main()
```

***EJERCICIO 5***

Ejercicio:

```
def mochila(n, w, val, weight):
    if n == 0 or w == 0:
        return 0
    if weight[n-1] > w:
        return mochila(n-1, w, val, weight)
    else:
        return max(val[n-1] + mochila(n-1, w-weight[n-1], val, weight), mochila(n-1, w, val, weight))

def main():
    precio = [103, 60, 70, 5, 15]
    pesos = [12, 23, 11, 15, 7]
    peso_maximo = 100
    n = len(precio)
    valor_maximo = mochila(n, peso_maximo, precio, pesos)
    print(valor_maximo)
```

Main:
```
from ej5 import *

if __name__ == '__main__':
    main()
```

***EJERCICIO 6***

```
import random
class Stormtrooper:
    def __init__(self, nombre, rango):
            self.nombre = nombre
            self.rango = rango
            print('Creado con éxito')
    def clasificacion(self):
        codigoLegion = self.nombre.split("-")[0]
        print('Codigo Legion: ' + codigoLegion)
        print('Identificador de Cohoerte: ' + self.nombre.split("-")[1][0])
        print('Identificador de Siglo: ' + self.nombre.split("-")[1][1])
        print('Identificador de Escuadra: ' + self.nombre.split("-")[1][2])
        print('Numero de Trooper: ' + self.nombre.split("-")[1][3])
    def __str__(self):
        return "Nombre: " + self.nombre + " Rango: " + str(self.rango)

#Deberá generar 2000 Stormtrooper siguiendo el formato de la imagen del primer ejecicio contemplando las siguientes legiones FL, TF, TK, CT, FN, FO y los dígitos generados de manera aleatoria;
hashTresDigitos = {}
listaLegiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FQ']
for i in range(2000):
    numRandom = random.randint(0, 5)
    listaNums = []
    for j in range(4):
        listaNums.append(str(random.randint(0, 9)))
    nums = ''.join(listaNums)
    tresDigitos = "".join(listaNums[1:])
    codLegion = listaLegiones[numRandom]
    stormtrooper = Stormtrooper(codLegion + '-' + nums, 7)
    if (hashTresDigitos.get(tresDigitos)):
        hashTresDigitos[tresDigitos][codLegion] = stormtrooper
    else:
        hashTresDigitos[tresDigitos] = {}
        hashTresDigitos[tresDigitos][codLegion] =stormtrooper

s = Stormtrooper('FN-2187', 7)
hashTresDigitos['187']['FN'] = s

if (hashTresDigitos.get('187').get('FN').nombre == 'FN-2187'):
    print('El trooper FN-2187 es el mismo que el FN-2187')

misionDesalto = []
misionExploracion = []

if (hashTresDigitos.get('781')):
    for i in hashTresDigitos.get('781').keys():
        misionDesalto.append(i)
if (hashTresDigitos.get('537')):
    for i in hashTresDigitos.get('537').keys():
        misionExploracion.append(i)

print('Mision desalto')
print(misionDesalto)
print('Mision Exploracion')
print(misionExploracion)

mExploracion = []
mExterminacion = []
for i in hashTresDigitos.keys():
    for j in hashTresDigitos.get(i).keys():
        if j == 'CT':
            mExploracion.append(hashTresDigitos[i][j])
        if j == 'TF':
            mExterminacion.append(hashTresDigitos[i][j])

print('Exploracion')
print(mExploracion)
print('Exterminacion')
print(mExterminacion)
```

***EJERCICIO 7***

Ejercicio:

```
class NodoArbol:
    def __init__(self, simbolo, freq):
        self.simbolo = simbolo
        self.freq = freq
        self.izq = None
        self.der = None
        self.padre = None

def ordenar_nodos(lista_nodos):
    lista_nodos =  sorted(lista_nodos, key = lambda x: x.simbolo) #ordenamos simbolos por orden alfabetico
    lista_nodos =  sorted(lista_nodos, key = lambda x: x.freq) #ordenamos frecuencias por simbolos anteriores
    return lista_nodos

def insertar_nodo(lista_nodos, nodo):
    for i in range(len(lista_nodos)):
        if nodo.freq < lista_nodos[i].freq:
            lista_nodos.insert(i, nodo)
        if i == len(lista_nodos) - 1:
            lista_nodos.append(nodo)
            break

    return lista_nodos

def crear_arbol(simbolos, frecuencias):
    nodos = []

    for i in range(len(simbolos)):
        nodos.append(NodoArbol(simbolos[i], frecuencias[i]))
    nodos = ordenar_nodos(nodos)

    while len(nodos) > 1:
        nodo = NodoArbol('XX', nodos[0].freq + nodos[1].freq)  #nodo padre con la suma de las frecuencias de los dos primeros nodos
        nodo.izq = nodos[0] #el primer nodo de la lista pasa a ser el hijo izquierdo del nodo padre
        nodo.izq.padre = nodo
        nodo.der = nodos[1] #el segundo de la lista pasa a ser el nodo dercho del padre
        nodo.der.padre = nodo
        nodos = insertar_nodo(nodos, nodo)
        nodos.pop(0) #eliminamos primer nodo
        nodos.pop(1) #eliminamos segundo nodo

    return nodos[0] #devolvemos el nodo raiz

def buscar(raiz, clave):
    p = 0

    if raiz is not None:
        if raiz.simbolo == clave:
            p = raiz
            return p
        elif p is None:
            p = buscar(raiz.izq, clave)
        elif p is None:
            p = buscar(raiz.der, clave)

    return p

def codificar(raiz, mensaje):
    codigo = []
    mensaje = mensaje[::-1] 

    for m in mensaje:
        nodo = buscar(raiz, m)
        while nodo.padre is not None:
            if nodo.padre.izq == nodo:
                codigo.append('0')
            else:
                codigo.append('1')
            nodo = nodo.padre
        codigo = codigo[::-1]
        return ''.join(codigo)

def decodificar(raiz, codigo):
    mensaje = []
    nodo = raiz
    for c in codigo:
        if nodo.der in None:
            mensaje.append(nodo.simbolo)
            nodo = raiz
        if c == '0':
            nodo = nodo.izq
        else:
            nodo = nodo.der
    
    mensaje.append(nodo.simbolo)
    mensaje = ''.join(mensaje)

    return mensaje
```

Main:
```
from ejercicio7 import *
if __name__ == '__main__':
    simbolos = ['A', 'F', '1', '3', '0', 'M', 'T']
    frecuencias = [0.2, 0.17, 0.13, 0.21, 0.05, 0.09, 0.15]
    raiz = crear_arbol(simbolos, frecuencias)
    print('\nObtenemos los siguientes códigos por cada símbolo: ')
    print('A: ', codificar('A', raiz))
    print('F: ', codificar('F', raiz))
    print('1: ', codificar('1', raiz))
    print('3: ', codificar('3', raiz))
    print('0: ', codificar('0', raiz))
    print('M: ', codificar('M', raiz))
    print('T: ', codificar('T', raiz))
    print('\nCodificamos el mensaje MOTO: ', codificar('MOTO', raiz))
    print('\nDecodificamos el mensaje de la palabra inicial: ', decodificar(codificar('MOTO', raiz), raiz), '\n')
```
***EJERCICIO 8***
```
import networkx as nx
import random

g = nx.Graph()   #grafo vacío
planetas = ['Alderaan', 'Endor', 'Dagobah', 'Hoth', 'Tatooine', 'Kamino', 'Naboo', 'Mustafar', 'Scarif', 'Bespin', 'Cantonica', 'DQar', 'Dantooine', 'Atollon', 'Jedha', 'Corellia', 'Coruscant']

g.add_node('Alderaan')
g.add_node('Endor')
g.add_node('Dagobah')
g.add_node('Hoth')
g.add_node('Tatooine')
g.add_node('Kamino')
g.add_node('Naboo')
g.add_node('Mustafar')
g.add_node('Scarif')
g.add_node('Bespin')
g.add_node('Cantonica')
g.add_node('DQar')
g.add_node('Dantooine')
g.add_node('Atollon')
g.add_node('Jedha')
g.add_node('Corellia')
g.add_node('Coruscant')

#generamso al menos 4 aristas
for node in g.nodes():
    for i in range(4):
        other_node = random.choice(list(g.nodes()))   #elegimos al azor otro nodo (planeta)
        while other_node == node:     #si es el mismo, volvemos a elegir
            other_node = random.choice(list(g.nodes()))
        weight = random.randint(1, 10)   #elegimos un peso al azar
        g.add_edge(node, other_node, weight=weight)   #agregamos la arista entre el nodo actual y el nodo elegido

t = nx.minimum_spanning_tree(g)   #obtenemos el arbol de expansion minima

#distancias
distance1 = nx.shortest_path_length(t, source = 'Tatooine', target='Dagobah', weight='weight')   #obtenemos la distancia entre Tatooine y Dagobah
distance2 = nx.shortest_path_length(t, source = 'Alderaan', target='Endor', weight='weight')
distance3 = nx.shortest_path_length(t, source = 'Hoth', target='Tatooine', weight='weight')

print(distance1)
print(distance2)
print(distance3)

#determinamos todos los planetas a los que se puede llegar desde Tatooine
neighbors =list(t.neighbors('Tatooine'))   #obtenemos los vecinos de Tatooine
print('Los planetas a los que se puede llegar desde Tatooine son: ', neighbors)
```
