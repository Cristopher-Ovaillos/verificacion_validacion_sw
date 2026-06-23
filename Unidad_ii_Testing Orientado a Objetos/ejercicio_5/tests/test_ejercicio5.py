import pytest
from flota.gestor_flota import GestorFlota

def test_unicidad_sing():
    instancia1 = GestorFlota.get_instancia()
    instancia2 = GestorFlota.get_instancia()
    assert instancia1 is instancia2
