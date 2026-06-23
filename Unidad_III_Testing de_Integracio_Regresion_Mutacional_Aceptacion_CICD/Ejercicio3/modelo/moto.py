# Proveniencia: Copiado de Unidad_III/Ejercicio2/modelo/moto.py
# Original:      Creado en Ejercicio 2 (nueva subclase Vehiculo)
from modelo.auto import EstadoVehiculo


class Moto:
    def __init__(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('km_actuales no puede ser negativo')
        if cilindrada <= 0:
            raise ValueError('cilindrada debe ser positiva')
        self._patente    = patente
        self._marca      = marca
        self._anio       = anio
        self._km         = km_actuales
        self._cilindrada = cilindrada
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def asignar(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,300]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 300:
            raise ValueError('km_estimados fuera de rango para moto')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Moto {self._patente} asignada a {legajo_conductor} por {km_estimados} km'

    def liberar(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('La moto no está en uso')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def get_estado(self) -> EstadoVehiculo:
        return self._estado

    def get_km(self) -> float:
        return self._km

    def get_patente(self) -> str:
        return self._patente

    def get_conductor(self):
        return self._conductor
