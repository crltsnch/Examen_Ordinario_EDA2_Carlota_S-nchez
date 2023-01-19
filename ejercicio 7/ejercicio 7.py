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

def crear_arbol(simbolo, freq):
    nodos = []

    for i in range(len(simbolo)):
        nodos.append(NodoArbol(simbolo[i], freq[i]))
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
    if p is not None:
        if raiz.simbolo == clave:
            p = raiz
        elif p is None:
