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