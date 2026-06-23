import pytest
from modelo.moto import Moto
from modelo.camion import Camion
from modelo.auto import EstadoVehiculo


@pytest.fixture(scope="function")
def moto_valida():
    return Moto(patente="MOTO123", marca="Honda", anio=2022,
                km_actuales=50.0, cilindrada=150)


@pytest.fixture(scope="function")
def camion_valido():
    return Camion(patente="CAM1234", marca="Scania", anio=2021,
                  km_actuales=1000.0, capacidad_carga=10000)


class TestNoRegresionMoto:

    def test_moto_asignar_300_km_limite(self, moto_valida):
        """Moto con 300 km debe funcionar (su límite es 300, no 500 u 800)."""
        resultado = moto_valida.asignar("L-010", 300.0)
        assert moto_valida.get_estado() == EstadoVehiculo.EN_USO
        assert moto_valida.get_conductor() == "L-010"
        assert "300" in resultado

    def test_moto_asignar_301_rechazado(self, moto_valida):
        """301 km excede el límite de Moto (300)."""
        with pytest.raises(ValueError):
            moto_valida.asignar("L-011", 301.0)

    def test_moto_liberar_tras_asignar(self, moto_valida):
        """Moto: ciclo completo asignar/liberar."""
        km_inicial = moto_valida.get_km()
        moto_valida.asignar("L-012", 100.0)
        moto_valida.liberar(80.0)
        assert moto_valida.get_estado() == EstadoVehiculo.DISPONIBLE
        assert moto_valida.get_km() == km_inicial + 80.0


class TestNoRegresionCamion:

    def test_camion_asignar_2000_km_limite(self, camion_valido):
        """Camión con 2000 km debe funcionar (su límite es 2000)."""
        resultado = camion_valido.asignar("L-020", 2000.0)
        assert camion_valido.get_estado() == EstadoVehiculo.EN_USO
        assert camion_valido.get_conductor() == "L-020"
        assert "2000" in resultado

    def test_camion_asignar_2001_rechazado(self, camion_valido):
        """2001 km excede el límite de Camión (2000)."""
        with pytest.raises(ValueError):
            camion_valido.asignar("L-021", 2001.0)

    def test_camion_liberar_tras_asignar(self, camion_valido):
        """Camión: ciclo completo asignar/liberar."""
        km_inicial = camion_valido.get_km()
        camion_valido.asignar("L-022", 500.0)
        camion_valido.liberar(450.0)
        assert camion_valido.get_estado() == EstadoVehiculo.DISPONIBLE
        assert camion_valido.get_km() == km_inicial + 450.0
