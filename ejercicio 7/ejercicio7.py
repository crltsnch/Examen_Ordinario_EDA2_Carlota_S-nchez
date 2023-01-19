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
        