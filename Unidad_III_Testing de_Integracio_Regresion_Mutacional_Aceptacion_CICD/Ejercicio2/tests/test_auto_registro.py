import pytest
from modelo.auto import Auto, EstadoVehiculo
from modelo.registro_kilometraje import RegistroKilometraje


@pytest.fixture(scope="function")
def cluster_auto_registro():
    registro = RegistroKilometraje()
    auto = Auto(patente='piplup123', marca='toyota', anio='2026',
                km_actuales=0.0, num_puertas=5)
    assert auto.get_estado() == EstadoVehiculo.DISPONIBLE
    assert registro.obtener_km('piplup123') == 0.0
    return auto, registro


class TestTPrime_ClusterAutoRegistro:

    def test_1a_flujo_asignar_liberar_registrar(self, cluster_auto_registro):
        auto, registro = cluster_auto_registro
        patente = auto.get_patente()
        km_recorridos = 150.0
        km_previo = registro.obtener_km(patente)

        auto.asignar(
            legajo_conductor='fai-3162',
            km_estimados=200.0
        )
        assert auto.get_estado() == EstadoVehiculo.EN_USO

        auto.liberar(km_recorridos=km_recorridos)
        registro.registrar(patente, km_recorridos)

        assert auto.get_estado() == EstadoVehiculo.DISPONIBLE
        assert registro.obtener_km(patente) == km_previo + km_recorridos
        assert registro.obtener_km(patente) >= 0

    def test_1b_dos_viajes_seguidos(self, cluster_auto_registro):
        auto, registro = cluster_auto_registro
        patente = auto.get_patente()

        km_viaje_1 = 100.0
        km_viaje_2 = 80.0

        auto.asignar(
            legajo_conductor='fai-3162',
            km_estimados=150.0
        )
        auto.liberar(km_recorridos=km_viaje_1)
        registro.registrar(patente, km_viaje_1)
        assert auto.get_estado() == EstadoVehiculo.DISPONIBLE

        auto.asignar(
            legajo_conductor='fai-3169',
            km_estimados=150.0
        )
        auto.liberar(km_recorridos=km_viaje_2)
        registro.registrar(patente, km_viaje_2)

        assert registro.obtener_km(patente) == km_viaje_1 + km_viaje_2
        assert auto.get_estado() == EstadoVehiculo.DISPONIBLE
        assert registro.obtener_km(patente) >= 0
