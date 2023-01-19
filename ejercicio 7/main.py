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
