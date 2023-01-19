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
            