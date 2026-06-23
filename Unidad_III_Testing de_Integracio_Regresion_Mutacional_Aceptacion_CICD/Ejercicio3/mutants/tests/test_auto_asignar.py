
#TestSuiteTP2_Auto Unidad_II/tests/test_ejercicio1.py
#TestNuevoLimite800 Unidad_III/Ejercicio2/tests/test_regresion_cambio_a.py
#TestNoRegresionMotoCamion Unidad_III/Ejercicio2/tests/test_no_regresion_moto_camion.py
import pytest
from modelo.auto import Auto, EstadoVehiculo
from modelo.moto import Moto
from modelo.camion import Camion


@pytest.fixture(scope="function")
def auto_valido():
    return Auto(patente="ABC123", marca="Toyota",
                anio=2020, km_actuales=200.0, num_puertas=4)

@pytest.fixture(scope="function")
def moto_valida():
    return Moto(patente="MOTO123", marca="Honda", anio=2022,
                km_actuales=50.0, cilindrada=150)

@pytest.fixture(scope="function")
def camion_valido():
    return Camion(patente="CAM1234", marca="Scania", anio=2021,
                  km_actuales=1000.0, capacidad_carga=10000)


class TestSuiteTP2_Auto:

    def test_3a_asignar_km_limite_inferior(self, auto_valido):
        legajo = "L-001"
        km = 1.0
        resultado = auto_valido.asignar(legajo, km)
        assert auto_valido.get_estado() == EstadoVehiculo.EN_USO
        assert auto_valido.get_conductor() == legajo

    def test_3b_asignar_km_limite_superior_500(self, auto_valido):
        legajo = "L-002"
        resultado = auto_valido.asignar(legajo, 500.0)
        assert auto_valido.get_estado() == EstadoVehiculo.EN_USO
        assert auto_valido.get_conductor() == legajo

    def test_3c_asignar_km_cero(self, auto_valido):
        estado_inicial = auto_valido.get_estado()
        with pytest.raises(ValueError):
            auto_valido.asignar("L-003", 0.0)
        assert auto_valido.get_estado() == estado_inicial

    def test_3d_asignar_desde_en_uso(self, auto_valido):
        auto_valido.asignar("L-004", 100.0)
        assert auto_valido.get_estado() == EstadoVehiculo.EN_USO
        with pytest.raises(PermissionError):
            auto_valido.asignar("L-005", 50.0)
        assert auto_valido.get_estado() == EstadoVehiculo.EN_USO

    def test_3e_liberar_km_150(self, auto_valido):
        auto_valido.asignar("L-006", 200.0)
        km_inicial = auto_valido.get_km()
        auto_valido.liberar(150.0)
        assert auto_valido.get_estado() == EstadoVehiculo.DISPONIBLE
        assert auto_valido.get_conductor() is None
        assert auto_valido.get_km() == km_inicial + 150.0

    def test_3f_liberar_desde_disponible(self, auto_valido):
        estado_inicial = auto_valido.get_estado()
        km_inicial = auto_valido.get_km()
        with pytest.raises(PermissionError):
            auto_valido.liberar(100.0)
        assert auto_valido.get_estado() == estado_inicial
        assert auto_valido.get_km() == km_inicial

    def test_3g_enviar_mantenimiento(self, auto_valido):
        auto_valido.enviar_mantenimiento()
        assert auto_valido.get_estado() == EstadoVehiculo.MANTENIMIENTO

    def test_3h_dar_de_baja(self, auto_valido):
        auto_valido.enviar_mantenimiento()
        auto_valido.dar_de_baja()
        assert auto_valido.get_estado() == EstadoVehiculo.BAJA


class TestNuevoLimite800:

    def test_asignar_800_km_en_el_limite(self, auto_valido):
        resultado = auto_valido.asignar("L-030", 800.0)
        assert auto_valido.get_estado() == EstadoVehiculo.EN_USO
        assert auto_valido.get_conductor() == "L-030"
        assert "800" in resultado

    def test_asignar_801_km_excede_limite(self, auto_valido):
        with pytest.raises(ValueError, match="fuera de rango"):
            auto_valido.asignar("L-031", 801.0)

    def test_asignar_1_km_sigue_siendo_valido(self, auto_valido):
        resultado = auto_valido.asignar("L-032", 1.0)
        assert auto_valido.get_estado() == EstadoVehiculo.EN_USO

    def test_asignar_500_km_ahora_es_valido(self, auto_valido):
        resultado = auto_valido.asignar("L-033", 500.0)
        assert auto_valido.get_estado() == EstadoVehiculo.EN_USO


class TestNoRegresionMotoCamion:

    def test_moto_asignar_300_km_limite(self, moto_valida):
        resultado = moto_valida.asignar("L-010", 300.0)
        assert moto_valida.get_estado() == EstadoVehiculo.EN_USO
        assert moto_valida.get_conductor() == "L-010"

    def test_moto_asignar_301_rechazado(self, moto_valida):
        with pytest.raises(ValueError):
            moto_valida.asignar("L-011", 301.0)

    def test_moto_liberar_tras_asignar(self, moto_valida):
        km_inicial = moto_valida.get_km()
        moto_valida.asignar("L-012", 100.0)
        moto_valida.liberar(80.0)
        assert moto_valida.get_estado() == EstadoVehiculo.DISPONIBLE
        assert moto_valida.get_km() == km_inicial + 80.0

    def test_camion_asignar_2000_km_limite(self, camion_valido):
        resultado = camion_valido.asignar("L-020", 2000.0)
        assert camion_valido.get_estado() == EstadoVehiculo.EN_USO

    def test_camion_asignar_2001_rechazado(self, camion_valido):
        with pytest.raises(ValueError):
            camion_valido.asignar("L-021", 2001.0)

    def test_camion_liberar_tras_asignar(self, camion_valido):
        km_inicial = camion_valido.get_km()
        camion_valido.asignar("L-022", 500.0)
        camion_valido.liberar(450.0)
        assert camion_valido.get_estado() == EstadoVehiculo.DISPONIBLE
        assert camion_valido.get_km() == km_inicial + 450.0
