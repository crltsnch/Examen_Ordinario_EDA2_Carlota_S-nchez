from ej1 import *

if __name__ == '__main__':
    stormtrooper = Stormtroopers('AK-3654', 7)
    print(stormtrooper.nombre)
    print(stormtrooper.rango)
    stormtrooper.clasificacion()
    print(stormtrooper.nombre.split("-")[0])
    print(stormtrooper.nombre.split("-")[1][0])
    print(stormtrooper.nombre.split("-")[1][1])
    print(stormtrooper.nombre.split("-")[1][2])
    print(stormtrooper.nombre.split("-")[1][3])
