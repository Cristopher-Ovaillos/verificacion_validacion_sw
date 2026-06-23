import pytest
from flota.gestor_flota import GestorFlota
from unittest.mock import MagicMock

vehiculo_mock = MagicMock()
vehiculo_mock.get_patente.return_value = "ABC123"


@pytest.fixture(scope='function')
def gestor_limpio():
    GestorFlota._reset_para_tests()
    yield GestorFlota.get_instancia()
    GestorFlota._reset_para_tests()


def test_1_limpio(gestor_limpio):
    gestor_limpio.registrar(vehiculo_mock)
    assert len(gestor_limpio._vehiculos) == 1


def test_2_limpio(gestor_limpio):
    gestor_limpio.registrar(vehiculo_mock)
    assert len(gestor_limpio._vehiculos) == 1
