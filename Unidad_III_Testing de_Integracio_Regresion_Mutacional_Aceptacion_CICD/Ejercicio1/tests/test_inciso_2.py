import pytest
from unittest.mock import MagicMock
from flota.auto import Auto, EstadoVehiculo
from flota.registro_kilometraje import RegistroKilometraje
from flota.servicio_mantenimiento import ServicioMantenimiento

@pytest.fixture(scope="function")
def cluster_servicio_con_mock():
    #Cluster {ServicioMantenimiento} con MagicMock para RegistroKilometraje
    mock_registro = MagicMock()
    mock_registro.obtener_km.return_value = 5200.0
    servicio = ServicioMantenimiento(registro_km=mock_registro)
    return servicio, mock_registro


@pytest.fixture(scope="function")
def auto_en_mantenimiento():
    #Auto ya transicionado a MANTENIMIENTO (precond. de ingresar()).
    auto = Auto(patente='ABC123', marca='Toyota', anio=2020,
                km_actuales=0.0, num_puertas=4)
    auto.enviar_mantenimiento()
    assert auto.get_estado() == EstadoVehiculo.MANTENIMIENTO
    return auto

class TestCluster2_ServicioMantenimientoConMock:

    def test_2a_ingresar_exitoso_llama_obtener_km_con_patente_correcta(
            self, cluster_servicio_con_mock, auto_en_mantenimiento):
        servicio, mock_registro = cluster_servicio_con_mock
        auto = auto_en_mantenimiento
        patente_esperada = auto.get_patente()

        resultado = servicio.ingresar(auto) #pide el km actual del auto registrado
        #entonces debe hacerlo con tal patente, de lo contrario puede haebr bugs llamas
        mock_registro.obtener_km.assert_called_once_with(patente_esperada) # viene de unnitest y lo que buscamos es q ingresar(auto) 
        #genere tal resultado, y que dentro de ingresar se use el registro kilometraje correctamente. Un assert solo, verifica 
        #lo que genera tal resultado esperado pero nada sobre como se hizo internmaente.
        assert patente_esperada in resultado
        assert '5200.0' in resultado

    def test_2b_ingresar_vehiculo_no_en_mantenimiento_lanza_error_y_mock_no_llamado(
            self, cluster_servicio_con_mock):
        servicio, mock_registro = cluster_servicio_con_mock
        auto_disponible = Auto(patente='XYZ999', marca='Ford', anio=2021,
                                km_actuales=0.0, num_puertas=2)
        assert auto_disponible.get_estado() == EstadoVehiculo.DISPONIBLE

        with pytest.raises(PermissionError):
            servicio.ingresar(auto_disponible)

        mock_registro.obtener_km.assert_not_called()


