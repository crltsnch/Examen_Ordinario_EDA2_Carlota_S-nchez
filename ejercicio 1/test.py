import pytest
from ej1 import Stormtroopers

def test_stormtrooper():
    stormtrooper = Stormtroopers('AK-3654', 7)
    assert stormtrooper.nombre == 'AK-3654'
    assert stormtrooper.rango == 7
    stormtrooper.clasificacion()
    assert stormtrooper.nombre.split("-")[0] == "AK"
    assert stormtrooper.nombre.split("-")[1][0] == "3"
    assert stormtrooper.nombre.split("-")[1][1] == "6"
    assert stormtrooper.nombre.split("-")[1][2] == "5"
    assert stormtrooper.nombre.split("-")[1][3] == "4"

