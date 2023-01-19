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

