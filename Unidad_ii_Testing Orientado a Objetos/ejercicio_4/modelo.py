# clase Auto con invariante de estado
# basado en la def 2.2 y el alg 2.1

from enum import Enum


class EstadoVehiculo(Enum):
    DISPONIBLE = "disponible"
    EN_USO = "en_uso"
    MANTENIMIENTO = "mantenimiento"


class Auto:
    # invariantes:
    #   len(_patente) >= 6
    #   _km >= 0
    #   _puertas in {2, 4, 5}
    #   _estado in EstadoVehiculo
    #   (_conductor is None) == (_estado != EN_USO)

    def __init__(self, patente: str, km: int, puertas: int, estado: EstadoVehiculo):
        self._patente = patente
        self._km = km
        self._puertas = puertas
        self._estado = estado
        self._conductor = None

    def asignar(self, legajo_conductor: str, km_estimados: int) -> str:
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError(f"El vehiculo no esta disponible. Estado: {self._estado.value}")

        if km_estimados <= 0 or km_estimados > 500:
            raise ValueError(f"km estimados deben estar en (0, 500]. Recibido: {km_estimados}")

        if legajo_conductor == '' or len(legajo_conductor) < 4:
            raise ValueError(f"legajo del conductor debe tener al menos 4 caracteres. Recibido: '{legajo_conductor}'")

        self._estado = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor

        return f"Vehiculo {self._patente} asignado a {legajo_conductor} por {km_estimados} km"

    def get_estado(self) -> EstadoVehiculo:
        return self._estado

    def get_conductor(self) -> str:
        return self._conductor

    def get_patente(self) -> str:
        return self._patente

    def get_km(self) -> int:
        return self._km

    def get_puertas(self) -> int:
        return self._puertas

    def verificar_invariante(self) -> bool:
        if len(self._patente) < 6:
            return False

        if self._km < 0:
            return False

        if self._puertas not in {2, 4, 5}:
            return False

        if not isinstance(self._estado, EstadoVehiculo):
            return False

        conductor_nulo = (self._conductor is None)
        estado_no_en_uso = (self._estado != EstadoVehiculo.EN_USO)
        if conductor_nulo != estado_no_en_uso:
            return False

        return True
