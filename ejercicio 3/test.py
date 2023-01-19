from datetime import datetime
from ej3 import *

def test_ArtefactosValiosos_init():
    artefasto = ArtefactosValiosos('Diamante', 50, 500, '08/31/2024')
    assert artefasto.nombre == 'Diamante'
    assert artefasto.peso == 50
    assert artefasto.precio == 500
    assert artefasto.fechaCaducidad == '08/31/2024'

def test_ArtefactosValiosos_str():
    artefacto = ArtefactosValiosos('Diamante', 50, 500, '08/31/2024')
    assert str(artefacto) == 'Nombre: Diamante Peso: 50 Precio: 500 Fecha de caducidad: 08/31/2024'

def test_sortByDate():
    lista = [ArtefactosValiosos('Diamante', 50, 500, '08/31/2024'),
ArtefactosValiosos('Esmeralda', 50, 500, '07/28/2023'),
ArtefactosValiosos('Perla', 50, 500, '09/30/2025')]
    lista.sort(key=sortByDate)
    assert lista[0].nombre == 'Esmeralda'
    assert lista[1].nombre == 'Diamante'