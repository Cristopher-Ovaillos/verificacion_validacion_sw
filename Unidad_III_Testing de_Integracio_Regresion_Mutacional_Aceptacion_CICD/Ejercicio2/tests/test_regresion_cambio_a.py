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


class TestNuevoLimite800:

    def test_asignar_800_km_en_el_limite(self, auto_valido):
        #800 km debe ser aceptado (nuevo límite superior del Cambio A)
        resultado = auto_valido.asignar("L-030", 800.0)
        assert auto_valido.get_estado() == EstadoVehiculo.EN_USO
        assert auto_valido.get_conductor() == "L-030"
        assert "800" in resultado

    def test_asignar_801_km_excede_limite(self, auto_valido):
        #801 km debe ser rechazado (excede el nuevo límite de 800)
        with pytest.raises(ValueError, match="fuera de rango"):
            auto_valido.asignar("L-031", 801.0)

    def test_asignar_1_km_sigue_siendo_valido(self, auto_valido):
        #1 km (borde inferior) sigue funcionando como antes.
        resultado = auto_valido.asignar("L-032", 1.0)
        assert auto_valido.get_estado() == EstadoVehiculo.EN_USO
        assert auto_valido.get_conductor() == "L-032"

    def test_asignar_500_km_ahora_es_valido(self, auto_valido):
        #500 km ahora funciona (el bug >= 500 se corrigió con el cambio).
        resultado = auto_valido.asignar("L-033", 500.0)
        assert auto_valido.get_estado() == EstadoVehiculo.EN_USO
        assert auto_valido.get_conductor() == "L-033"


class TestNoRegresionConCambioA:

    def test_moto_sigue_funcionando_con_300(self, moto_valida):
        #Verifica que el cambio en Auto no rompió Moto."""
        resultado = moto_valida.asignar("L-040", 300.0)
        assert moto_valida.get_estado() == EstadoVehiculo.EN_USO
        assert "MOTO123" in resultado

    def test_camion_sigue_funcionando_con_2000(self, camion_valido):
        #Verifica que el cambio en Auto no rompió Camión."""
        resultado = camion_valido.asignar("L-041", 2000.0)
        assert camion_valido.get_estado() == EstadoVehiculo.EN_USO
        assert "CAM1234" in resultado
