import pytest
from flota.gestor_flota import GestorFlota
from unittest.mock import MagicMock

vehiculo_mock = MagicMock()
vehiculo_mock.get_patente.return_value = "ABC123"


def test_A_agrega_vehiculo():
    gestor = GestorFlota.get_instancia()
    gestor.registrar(vehiculo_mock)
    assert len(gestor._vehiculos) == 1


def test_B_gestor_vacio():
    gestor = GestorFlota.get_instancia()
    gestor.registrar(vehiculo_mock)
