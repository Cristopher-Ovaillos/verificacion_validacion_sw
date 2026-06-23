# Proveniencia: Copiado de Unidad_III/Ejercicio1/flota/servicio_mantenimiento.py
# Original:      Nuevo en Unidad III
class ServicioMantenimiento:
    def __init__(self, registro_km):
        self._vehiculos_en_taller = []
        self._registro = registro_km

    def ingresar(self, vehiculo) -> str:
        if vehiculo.get_estado().name != 'MANTENIMIENTO':
            raise PermissionError('El vehículo debe estar en estado MANTENIMIENTO')
        patente = vehiculo.get_patente()
        self._vehiculos_en_taller.append(patente)
        km_actual = self._registro.obtener_km(patente)
        return f'Vehículo {patente} ingresado al taller. KM actuales: {km_actual}'

    def liberar(self, vehiculo) -> None:
        patente = vehiculo.get_patente()
        if patente not in self._vehiculos_en_taller:
            raise KeyError('Vehículo no está en el taller')
        self._vehiculos_en_taller.remove(patente)
        # BUG intencional: debería ser vehiculo.liberar(0) o similar
        vehiculo.enviar_mantenimiento()
