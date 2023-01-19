# Examen_Ordinario_EDA2_Carlota_S-nchez
***Ejercicio 1***:

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
    
***Ejercicio 7***:

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
***Ejercicio 8***:
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
