
import pytest
from unittest.mock import MagicMock
from flota.auto import Auto, EstadoVehiculo
from flota.registro_kilometraje import RegistroKilometraje
from flota.servicio_mantenimiento import ServicioMantenimiento

@pytest.fixture(scope="function")
def cluster_servicio_con_mock():
    #Cluster {ServicioMantenimiento} con MagicMock para RegistroKilometraje.
    mock_registro = MagicMock()
    mock_registro.obtener_km.return_value = 5200.0
    servicio = ServicioMantenimiento(registro_km=mock_registro)
    return servicio, mock_registro
@pytest.fixture(scope="function")
def auto_en_mantenimiento():
    #Auto ya transicionado a MANTENIMIENTO (precond. de ingresar()).#
    auto = Auto(patente='ABC123', marca='Toyota', anio=2020,
                km_actuales=0.0, num_puertas=4)
    auto.enviar_mantenimiento()
    assert auto.get_estado() == EstadoVehiculo.MANTENIMIENTO
    return auto

class TestBugEnLiberar:

    def test_3_liberar_del_taller_debe_dejar_vehiculo_disponible(
            self, cluster_servicio_con_mock, auto_en_mantenimiento):
        servicio, mock_registro = cluster_servicio_con_mock
        auto = auto_en_mantenimiento
        servicio.ingresar(auto)

        servicio.liberar(auto)   # aquí se manifiesta el bug

        assert auto.get_estado() == EstadoVehiculo.DISPONIBLE