
import pytest
from unittest.mock import MagicMock
from flota.auto import Auto, EstadoVehiculo
from flota.registro_kilometraje import RegistroKilometraje
from flota.servicio_mantenimiento import ServicioMantenimiento

class TestEscenarioCompleto:

    def test_5_flujo_completo_evidencia_bug_al_salir_del_taller(self):
        registro_real = RegistroKilometraje()
        mock_registro_servicio = MagicMock()
        mock_registro_servicio.obtener_km.return_value = 380.0

        auto = Auto(patente='ABC123', marca='Toyota', anio=2020,
                    km_actuales=0.0, num_puertas=4)
        servicio = ServicioMantenimiento(registro_km=mock_registro_servicio)

        auto.asignar(legajo_conductor='L-001', km_estimados=450)
        assert auto.get_estado() == EstadoVehiculo.EN_USO
        auto.liberar(km_recorridos=380)
        registro_real.registrar('ABC123', 380)
        assert auto.get_estado() == EstadoVehiculo.DISPONIBLE
        assert registro_real.obtener_km('ABC123') == 380.0

        auto.enviar_mantenimiento()
        assert auto.get_estado() == EstadoVehiculo.MANTENIMIENTO

        servicio.ingresar(auto)
        assert 'ABC123' in servicio._vehiculos_en_taller

        servicio.liberar(auto)   # aquí se manifiesta el bug

        assert auto.get_estado() == EstadoVehiculo.DISPONIBLE