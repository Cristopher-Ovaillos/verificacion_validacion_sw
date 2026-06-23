# Proveniencia: Copiado de Unidad_III/Ejercicio2/modelo/camion.py
# Original:      Creado en Ejercicio 2 (nueva subclase Vehiculo)
from modelo.auto import EstadoVehiculo


class Camion:
    def __init__(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('km_actuales no puede ser negativo')
        if capacidad_carga <= 0:
            raise ValueError('capacidad_carga debe ser positiva')
        self._patente         = patente
        self._marca           = marca
        self._anio            = anio
        self._km              = km_actuales
        self._capacidad_carga = capacidad_carga
        self._carga_actual    = 0.0
        self._estado          = EstadoVehiculo.DISPONIBLE
        self._conductor       = None

    def asignar(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,2000]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 2000:
            raise ValueError('km_estimados fuera de rango para camión')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Camión {self._patente} asignado a {legajo_conductor} por {km_estimados} km'

    def liberar(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('El camión no está en uso')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def cargar(self, peso: float) -> None:
        if peso <= 0:
            raise ValueError('peso debe ser positivo')
        if self._carga_actual + peso > self._capacidad_carga:
            raise ValueError('supera la capacidad de carga')
        self._carga_actual += peso

    def get_estado(self) -> EstadoVehiculo:
        return self._estado

    def get_km(self) -> float:
        return self._km

    def get_patente(self) -> str:
        return self._patente

    def get_conductor(self):
        return self._conductor
