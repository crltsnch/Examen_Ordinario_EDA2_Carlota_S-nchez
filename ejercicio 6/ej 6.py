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
    for j in range(4):
        listaNums.append(str(random.randint(0, 9)))
    nums = ''.join(listaNums)
    tresDigitos = "".join(listaNums[1:])
    codLegion = listaLegiones[numRandom]
    stormtrooper = Stormtrooper(codLegion + '-' + nums, 7)
    if (hashTresDigitos.get(tresDigitos)):
        hashTresDigitos[tresDigitos][codLegion] = stormtrooper
    else:
        hashTresDigitos[tresDigitos] = {}
        hashTresDigitos[tresDigitos][codLegion] =stormtrooper

s = Stormtrooper('FN-2187', 7)
hashTresDigitos['187']['FN'] = s

if (hashTresDigitos.get('187').get('FN').nombre == 'FN-2187'):
    print('El trooper FN-2187 es el mismo que el FN-2187')

misionDesalto = []
misionExploracion = []

if (hashTresDigitos.get('781')):
    for i in hashTresDigitos.get('781').keys():
        misionDesalto.append(i)
if (hashTresDigitos.get('537')):
    for i in hashTresDigitos.get('537').keys():
        misionExploracion.append(i)

print('Mision desalto')
print(misionDesalto)
print('Mision Exploracion')
print(misionExploracion)
