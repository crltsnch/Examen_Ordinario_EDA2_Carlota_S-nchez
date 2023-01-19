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