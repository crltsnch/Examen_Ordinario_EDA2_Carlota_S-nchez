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
    return datetime.strptime(elem.fechaCaducidad, '%d/%m/%Y')

lista = [ArtefactosValiosos('Diamante', 50, 500, '08/31/2024'),
ArtefactosValiosos('Esmeralda', 50, 500, '07/28/2023'),
ArtefactosValiosos('Perla', 50, 500, '09/30/2025')]
lista.sort(key=sortByDate)
for stormtrooper in lista:
    print(stormtrooper)

print('Precio cambiado')
lista[0].precio = 400
print(lista[0]) 