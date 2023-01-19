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
    for i in rang

