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

#Deberá generar 2000 Stormtrooper siguiendo el formato de la imagen del primer ejecicio contemplando las siguientes legiones FL, TF, TK, CT, FN, FO y los dígitos generados de manera aleatoria;
hashTresDigitos = {}
listaLegiones = ['FL', 'TF', 'TK', 'CT', 'FN', 'FQ']
for i in range(2000):
    numRandom = random.randint(0, 5)
    listaNums = []
    for i in range(4):
        listaNums.append(random.randint(0, 9))

    nums = ''.join(listaNums)
    codLegion = listaLegiones[numRandom]
    Stormtrooper = Stormtrooper(codLegion + '-' + nums, 7)
    print(Stormtrooper)


