
#Sin _reset_para_tests() entocnes el estado del Singleton persiste entre tests
#el orden de ejecucio puede producir falsos positivos o negativos

import pytest
from modelo.auto import Auto
from modelo.gestor_flota import GestorFlota

# dos fixture donde retornamos la instancia almacenada en la clase.

@pytest.fixture(scope="function")
def gestor_sin_reset():
    #sin reset estado del test anterior persiste.
    return GestorFlota.get_instancia()

@pytest.fixture(scope="function")
def gestor_con_reset():
    #Singleton CON reset — cada test empieza y termina limpio
    GestorFlota._reset_para_tests()  # estado inicial conocido
    gestor = GestorFlota.get_instancia()
    yield gestor
    GestorFlota._reset_para_tests()  # limpia despues del test


@pytest.fixture(scope="function")
def auto_para_gestor():
    return Auto(patente="ABC123", marca="Toyota",
                anio=2020, km_actuales=200.0, num_puertas=4)


class TestContaminacionSinReset:
#esto se ejecuta en orden
    def test_primero_agrega_vehiculo(self, gestor_sin_reset, auto_para_gestor):
        gestor_sin_reset.registrar(auto_para_gestor)
        assert len(gestor_sin_reset._vehiculos) == 1

    def test_segundo_espera_vacio_pero_encuentra_uno(self, gestor_sin_reset):
        #esto deberia de fallar por contaminacio el test anterior dejo un vehiculo registrado
        assert len(gestor_sin_reset._vehiculos) == 0  # falla hay 1 del aanterior test

class TestSinContaminacionConReset:

    def test_primero_con_reset(self, gestor_con_reset, auto_para_gestor):
        gestor_con_reset.registrar(auto_para_gestor)
        assert len(gestor_con_reset._vehiculos) == 1

    def test_segundo_con_reset_esta_limpio(self, gestor_con_reset):
        #limpio para el sigueinte test
        assert len(gestor_con_reset._vehiculos) == 0  # aca pasa
