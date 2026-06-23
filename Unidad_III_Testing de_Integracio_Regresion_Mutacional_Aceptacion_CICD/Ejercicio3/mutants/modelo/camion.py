# Proveniencia: Copiado de Unidad_III/Ejercicio2/modelo/camion.py
# Original:      Creado en Ejercicio 2 (nueva subclase Vehiculo)
from modelo.auto import EstadoVehiculo


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁCamionǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁCamionǁasignar__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCamionǁliberar__mutmut: MutantDict = {}  # type: ignore
mutants_xǁCamionǁcargar__mutmut: MutantDict = {}  # type: ignore


class Camion:
    @_mutmut_mutated(mutants_xǁCamionǁ__init____mutmut)
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
    def xǁCamionǁ__init____mutmut_orig(self, patente: str, marca: str, anio: int,
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
    def xǁCamionǁ__init____mutmut_1(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente and len(patente) < 6:
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
    def xǁCamionǁ__init____mutmut_2(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if patente or len(patente) < 6:
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
    def xǁCamionǁ__init____mutmut_3(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) <= 6:
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
    def xǁCamionǁ__init____mutmut_4(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) < 7:
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
    def xǁCamionǁ__init____mutmut_5(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) < 6:
            raise ValueError(None)
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
    def xǁCamionǁ__init____mutmut_6(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) < 6:
            raise ValueError('XXPatente inválidaXX')
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
    def xǁCamionǁ__init____mutmut_7(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) < 6:
            raise ValueError('patente inválida')
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
    def xǁCamionǁ__init____mutmut_8(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) < 6:
            raise ValueError('PATENTE INVÁLIDA')
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
    def xǁCamionǁ__init____mutmut_9(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales <= 0:
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
    def xǁCamionǁ__init____mutmut_10(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 1:
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
    def xǁCamionǁ__init____mutmut_11(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError(None)
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
    def xǁCamionǁ__init____mutmut_12(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('XXkm_actuales no puede ser negativoXX')
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
    def xǁCamionǁ__init____mutmut_13(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('KM_ACTUALES NO PUEDE SER NEGATIVO')
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
    def xǁCamionǁ__init____mutmut_14(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('km_actuales no puede ser negativo')
        if capacidad_carga < 0:
            raise ValueError('capacidad_carga debe ser positiva')
        self._patente         = patente
        self._marca           = marca
        self._anio            = anio
        self._km              = km_actuales
        self._capacidad_carga = capacidad_carga
        self._carga_actual    = 0.0
        self._estado          = EstadoVehiculo.DISPONIBLE
        self._conductor       = None
    def xǁCamionǁ__init____mutmut_15(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('km_actuales no puede ser negativo')
        if capacidad_carga <= 1:
            raise ValueError('capacidad_carga debe ser positiva')
        self._patente         = patente
        self._marca           = marca
        self._anio            = anio
        self._km              = km_actuales
        self._capacidad_carga = capacidad_carga
        self._carga_actual    = 0.0
        self._estado          = EstadoVehiculo.DISPONIBLE
        self._conductor       = None
    def xǁCamionǁ__init____mutmut_16(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('km_actuales no puede ser negativo')
        if capacidad_carga <= 0:
            raise ValueError(None)
        self._patente         = patente
        self._marca           = marca
        self._anio            = anio
        self._km              = km_actuales
        self._capacidad_carga = capacidad_carga
        self._carga_actual    = 0.0
        self._estado          = EstadoVehiculo.DISPONIBLE
        self._conductor       = None
    def xǁCamionǁ__init____mutmut_17(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('km_actuales no puede ser negativo')
        if capacidad_carga <= 0:
            raise ValueError('XXcapacidad_carga debe ser positivaXX')
        self._patente         = patente
        self._marca           = marca
        self._anio            = anio
        self._km              = km_actuales
        self._capacidad_carga = capacidad_carga
        self._carga_actual    = 0.0
        self._estado          = EstadoVehiculo.DISPONIBLE
        self._conductor       = None
    def xǁCamionǁ__init____mutmut_18(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('km_actuales no puede ser negativo')
        if capacidad_carga <= 0:
            raise ValueError('CAPACIDAD_CARGA DEBE SER POSITIVA')
        self._patente         = patente
        self._marca           = marca
        self._anio            = anio
        self._km              = km_actuales
        self._capacidad_carga = capacidad_carga
        self._carga_actual    = 0.0
        self._estado          = EstadoVehiculo.DISPONIBLE
        self._conductor       = None
    def xǁCamionǁ__init____mutmut_19(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('km_actuales no puede ser negativo')
        if capacidad_carga <= 0:
            raise ValueError('capacidad_carga debe ser positiva')
        self._patente         = None
        self._marca           = marca
        self._anio            = anio
        self._km              = km_actuales
        self._capacidad_carga = capacidad_carga
        self._carga_actual    = 0.0
        self._estado          = EstadoVehiculo.DISPONIBLE
        self._conductor       = None
    def xǁCamionǁ__init____mutmut_20(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('km_actuales no puede ser negativo')
        if capacidad_carga <= 0:
            raise ValueError('capacidad_carga debe ser positiva')
        self._patente         = patente
        self._marca           = None
        self._anio            = anio
        self._km              = km_actuales
        self._capacidad_carga = capacidad_carga
        self._carga_actual    = 0.0
        self._estado          = EstadoVehiculo.DISPONIBLE
        self._conductor       = None
    def xǁCamionǁ__init____mutmut_21(self, patente: str, marca: str, anio: int,
                 km_actuales: float, capacidad_carga: float):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('km_actuales no puede ser negativo')
        if capacidad_carga <= 0:
            raise ValueError('capacidad_carga debe ser positiva')
        self._patente         = patente
        self._marca           = marca
        self._anio            = None
        self._km              = km_actuales
        self._capacidad_carga = capacidad_carga
        self._carga_actual    = 0.0
        self._estado          = EstadoVehiculo.DISPONIBLE
        self._conductor       = None
    def xǁCamionǁ__init____mutmut_22(self, patente: str, marca: str, anio: int,
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
        self._km              = None
        self._capacidad_carga = capacidad_carga
        self._carga_actual    = 0.0
        self._estado          = EstadoVehiculo.DISPONIBLE
        self._conductor       = None
    def xǁCamionǁ__init____mutmut_23(self, patente: str, marca: str, anio: int,
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
        self._capacidad_carga = None
        self._carga_actual    = 0.0
        self._estado          = EstadoVehiculo.DISPONIBLE
        self._conductor       = None
    def xǁCamionǁ__init____mutmut_24(self, patente: str, marca: str, anio: int,
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
        self._carga_actual    = None
        self._estado          = EstadoVehiculo.DISPONIBLE
        self._conductor       = None
    def xǁCamionǁ__init____mutmut_25(self, patente: str, marca: str, anio: int,
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
        self._carga_actual    = 1.0
        self._estado          = EstadoVehiculo.DISPONIBLE
        self._conductor       = None
    def xǁCamionǁ__init____mutmut_26(self, patente: str, marca: str, anio: int,
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
        self._estado          = None
        self._conductor       = None
    def xǁCamionǁ__init____mutmut_27(self, patente: str, marca: str, anio: int,
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
        self._conductor       = ""

    @_mutmut_mutated(mutants_xǁCamionǁasignar__mutmut)
    def asignar(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,2000]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 2000:
            raise ValueError('km_estimados fuera de rango para camión')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Camión {self._patente} asignado a {legajo_conductor} por {km_estimados} km'

    def xǁCamionǁasignar__mutmut_orig(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,2000]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 2000:
            raise ValueError('km_estimados fuera de rango para camión')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Camión {self._patente} asignado a {legajo_conductor} por {km_estimados} km'

    def xǁCamionǁasignar__mutmut_1(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,2000]."""
        if self._estado == EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 2000:
            raise ValueError('km_estimados fuera de rango para camión')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Camión {self._patente} asignado a {legajo_conductor} por {km_estimados} km'

    def xǁCamionǁasignar__mutmut_2(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,2000]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError(None)
        if km_estimados <= 0 or km_estimados > 2000:
            raise ValueError('km_estimados fuera de rango para camión')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Camión {self._patente} asignado a {legajo_conductor} por {km_estimados} km'

    def xǁCamionǁasignar__mutmut_3(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,2000]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('XXVehículo no disponibleXX')
        if km_estimados <= 0 or km_estimados > 2000:
            raise ValueError('km_estimados fuera de rango para camión')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Camión {self._patente} asignado a {legajo_conductor} por {km_estimados} km'

    def xǁCamionǁasignar__mutmut_4(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,2000]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 2000:
            raise ValueError('km_estimados fuera de rango para camión')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Camión {self._patente} asignado a {legajo_conductor} por {km_estimados} km'

    def xǁCamionǁasignar__mutmut_5(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,2000]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('VEHÍCULO NO DISPONIBLE')
        if km_estimados <= 0 or km_estimados > 2000:
            raise ValueError('km_estimados fuera de rango para camión')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Camión {self._patente} asignado a {legajo_conductor} por {km_estimados} km'

    def xǁCamionǁasignar__mutmut_6(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,2000]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 and km_estimados > 2000:
            raise ValueError('km_estimados fuera de rango para camión')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Camión {self._patente} asignado a {legajo_conductor} por {km_estimados} km'

    def xǁCamionǁasignar__mutmut_7(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,2000]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados < 0 or km_estimados > 2000:
            raise ValueError('km_estimados fuera de rango para camión')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Camión {self._patente} asignado a {legajo_conductor} por {km_estimados} km'

    def xǁCamionǁasignar__mutmut_8(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,2000]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 1 or km_estimados > 2000:
            raise ValueError('km_estimados fuera de rango para camión')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Camión {self._patente} asignado a {legajo_conductor} por {km_estimados} km'

    def xǁCamionǁasignar__mutmut_9(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,2000]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados >= 2000:
            raise ValueError('km_estimados fuera de rango para camión')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Camión {self._patente} asignado a {legajo_conductor} por {km_estimados} km'

    def xǁCamionǁasignar__mutmut_10(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,2000]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 2001:
            raise ValueError('km_estimados fuera de rango para camión')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Camión {self._patente} asignado a {legajo_conductor} por {km_estimados} km'

    def xǁCamionǁasignar__mutmut_11(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,2000]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 2000:
            raise ValueError(None)
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Camión {self._patente} asignado a {legajo_conductor} por {km_estimados} km'

    def xǁCamionǁasignar__mutmut_12(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,2000]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 2000:
            raise ValueError('XXkm_estimados fuera de rango para camiónXX')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Camión {self._patente} asignado a {legajo_conductor} por {km_estimados} km'

    def xǁCamionǁasignar__mutmut_13(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,2000]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 2000:
            raise ValueError('KM_ESTIMADOS FUERA DE RANGO PARA CAMIÓN')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Camión {self._patente} asignado a {legajo_conductor} por {km_estimados} km'

    def xǁCamionǁasignar__mutmut_14(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,2000]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 2000:
            raise ValueError('km_estimados fuera de rango para camión')
        self._estado    = None
        self._conductor = legajo_conductor
        return f'Camión {self._patente} asignado a {legajo_conductor} por {km_estimados} km'

    def xǁCamionǁasignar__mutmut_15(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,2000]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 2000:
            raise ValueError('km_estimados fuera de rango para camión')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = None
        return f'Camión {self._patente} asignado a {legajo_conductor} por {km_estimados} km'

    @_mutmut_mutated(mutants_xǁCamionǁliberar__mutmut)
    def liberar(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('El camión no está en uso')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁCamionǁliberar__mutmut_orig(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('El camión no está en uso')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁCamionǁliberar__mutmut_1(self, km_recorridos: float) -> None:
        if self._estado == EstadoVehiculo.EN_USO:
            raise PermissionError('El camión no está en uso')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁCamionǁliberar__mutmut_2(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError(None)
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁCamionǁliberar__mutmut_3(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('XXEl camión no está en usoXX')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁCamionǁliberar__mutmut_4(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('el camión no está en uso')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁCamionǁliberar__mutmut_5(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('EL CAMIÓN NO ESTÁ EN USO')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁCamionǁliberar__mutmut_6(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('El camión no está en uso')
        if km_recorridos <= 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁCamionǁliberar__mutmut_7(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('El camión no está en uso')
        if km_recorridos < 1:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁCamionǁliberar__mutmut_8(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('El camión no está en uso')
        if km_recorridos < 0:
            raise ValueError(None)
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁCamionǁliberar__mutmut_9(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('El camión no está en uso')
        if km_recorridos < 0:
            raise ValueError('XXkm_recorridos no puede ser negativoXX')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁCamionǁliberar__mutmut_10(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('El camión no está en uso')
        if km_recorridos < 0:
            raise ValueError('KM_RECORRIDOS NO PUEDE SER NEGATIVO')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁCamionǁliberar__mutmut_11(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('El camión no está en uso')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km = km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁCamionǁliberar__mutmut_12(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('El camión no está en uso')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km -= km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁCamionǁliberar__mutmut_13(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('El camión no está en uso')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = None
        self._conductor  = None

    def xǁCamionǁliberar__mutmut_14(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('El camión no está en uso')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = ""

    @_mutmut_mutated(mutants_xǁCamionǁcargar__mutmut)
    def cargar(self, peso: float) -> None:
        if peso <= 0:
            raise ValueError('peso debe ser positivo')
        if self._carga_actual + peso > self._capacidad_carga:
            raise ValueError('supera la capacidad de carga')
        self._carga_actual += peso

    def xǁCamionǁcargar__mutmut_orig(self, peso: float) -> None:
        if peso <= 0:
            raise ValueError('peso debe ser positivo')
        if self._carga_actual + peso > self._capacidad_carga:
            raise ValueError('supera la capacidad de carga')
        self._carga_actual += peso

    def xǁCamionǁcargar__mutmut_1(self, peso: float) -> None:
        if peso < 0:
            raise ValueError('peso debe ser positivo')
        if self._carga_actual + peso > self._capacidad_carga:
            raise ValueError('supera la capacidad de carga')
        self._carga_actual += peso

    def xǁCamionǁcargar__mutmut_2(self, peso: float) -> None:
        if peso <= 1:
            raise ValueError('peso debe ser positivo')
        if self._carga_actual + peso > self._capacidad_carga:
            raise ValueError('supera la capacidad de carga')
        self._carga_actual += peso

    def xǁCamionǁcargar__mutmut_3(self, peso: float) -> None:
        if peso <= 0:
            raise ValueError(None)
        if self._carga_actual + peso > self._capacidad_carga:
            raise ValueError('supera la capacidad de carga')
        self._carga_actual += peso

    def xǁCamionǁcargar__mutmut_4(self, peso: float) -> None:
        if peso <= 0:
            raise ValueError('XXpeso debe ser positivoXX')
        if self._carga_actual + peso > self._capacidad_carga:
            raise ValueError('supera la capacidad de carga')
        self._carga_actual += peso

    def xǁCamionǁcargar__mutmut_5(self, peso: float) -> None:
        if peso <= 0:
            raise ValueError('PESO DEBE SER POSITIVO')
        if self._carga_actual + peso > self._capacidad_carga:
            raise ValueError('supera la capacidad de carga')
        self._carga_actual += peso

    def xǁCamionǁcargar__mutmut_6(self, peso: float) -> None:
        if peso <= 0:
            raise ValueError('peso debe ser positivo')
        if self._carga_actual - peso > self._capacidad_carga:
            raise ValueError('supera la capacidad de carga')
        self._carga_actual += peso

    def xǁCamionǁcargar__mutmut_7(self, peso: float) -> None:
        if peso <= 0:
            raise ValueError('peso debe ser positivo')
        if self._carga_actual + peso >= self._capacidad_carga:
            raise ValueError('supera la capacidad de carga')
        self._carga_actual += peso

    def xǁCamionǁcargar__mutmut_8(self, peso: float) -> None:
        if peso <= 0:
            raise ValueError('peso debe ser positivo')
        if self._carga_actual + peso > self._capacidad_carga:
            raise ValueError(None)
        self._carga_actual += peso

    def xǁCamionǁcargar__mutmut_9(self, peso: float) -> None:
        if peso <= 0:
            raise ValueError('peso debe ser positivo')
        if self._carga_actual + peso > self._capacidad_carga:
            raise ValueError('XXsupera la capacidad de cargaXX')
        self._carga_actual += peso

    def xǁCamionǁcargar__mutmut_10(self, peso: float) -> None:
        if peso <= 0:
            raise ValueError('peso debe ser positivo')
        if self._carga_actual + peso > self._capacidad_carga:
            raise ValueError('SUPERA LA CAPACIDAD DE CARGA')
        self._carga_actual += peso

    def xǁCamionǁcargar__mutmut_11(self, peso: float) -> None:
        if peso <= 0:
            raise ValueError('peso debe ser positivo')
        if self._carga_actual + peso > self._capacidad_carga:
            raise ValueError('supera la capacidad de carga')
        self._carga_actual = peso

    def xǁCamionǁcargar__mutmut_12(self, peso: float) -> None:
        if peso <= 0:
            raise ValueError('peso debe ser positivo')
        if self._carga_actual + peso > self._capacidad_carga:
            raise ValueError('supera la capacidad de carga')
        self._carga_actual -= peso

    def get_estado(self) -> EstadoVehiculo:
        return self._estado

    def get_km(self) -> float:
        return self._km

    def get_patente(self) -> str:
        return self._patente

    def get_conductor(self):
        return self._conductor

mutants_xǁCamionǁ__init____mutmut['_mutmut_orig'] = Camion.xǁCamionǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_1'] = Camion.xǁCamionǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_2'] = Camion.xǁCamionǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_3'] = Camion.xǁCamionǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_4'] = Camion.xǁCamionǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_5'] = Camion.xǁCamionǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_6'] = Camion.xǁCamionǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_7'] = Camion.xǁCamionǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_8'] = Camion.xǁCamionǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_9'] = Camion.xǁCamionǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_10'] = Camion.xǁCamionǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_11'] = Camion.xǁCamionǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_12'] = Camion.xǁCamionǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_13'] = Camion.xǁCamionǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_14'] = Camion.xǁCamionǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_15'] = Camion.xǁCamionǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_16'] = Camion.xǁCamionǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_17'] = Camion.xǁCamionǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_18'] = Camion.xǁCamionǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_19'] = Camion.xǁCamionǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_20'] = Camion.xǁCamionǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_21'] = Camion.xǁCamionǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_22'] = Camion.xǁCamionǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_23'] = Camion.xǁCamionǁ__init____mutmut_23 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_24'] = Camion.xǁCamionǁ__init____mutmut_24 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_25'] = Camion.xǁCamionǁ__init____mutmut_25 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_26'] = Camion.xǁCamionǁ__init____mutmut_26 # type: ignore # mutmut generated
mutants_xǁCamionǁ__init____mutmut['xǁCamionǁ__init____mutmut_27'] = Camion.xǁCamionǁ__init____mutmut_27 # type: ignore # mutmut generated

mutants_xǁCamionǁasignar__mutmut['_mutmut_orig'] = Camion.xǁCamionǁasignar__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCamionǁasignar__mutmut['xǁCamionǁasignar__mutmut_1'] = Camion.xǁCamionǁasignar__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCamionǁasignar__mutmut['xǁCamionǁasignar__mutmut_2'] = Camion.xǁCamionǁasignar__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCamionǁasignar__mutmut['xǁCamionǁasignar__mutmut_3'] = Camion.xǁCamionǁasignar__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCamionǁasignar__mutmut['xǁCamionǁasignar__mutmut_4'] = Camion.xǁCamionǁasignar__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCamionǁasignar__mutmut['xǁCamionǁasignar__mutmut_5'] = Camion.xǁCamionǁasignar__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCamionǁasignar__mutmut['xǁCamionǁasignar__mutmut_6'] = Camion.xǁCamionǁasignar__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCamionǁasignar__mutmut['xǁCamionǁasignar__mutmut_7'] = Camion.xǁCamionǁasignar__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCamionǁasignar__mutmut['xǁCamionǁasignar__mutmut_8'] = Camion.xǁCamionǁasignar__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCamionǁasignar__mutmut['xǁCamionǁasignar__mutmut_9'] = Camion.xǁCamionǁasignar__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCamionǁasignar__mutmut['xǁCamionǁasignar__mutmut_10'] = Camion.xǁCamionǁasignar__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCamionǁasignar__mutmut['xǁCamionǁasignar__mutmut_11'] = Camion.xǁCamionǁasignar__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCamionǁasignar__mutmut['xǁCamionǁasignar__mutmut_12'] = Camion.xǁCamionǁasignar__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCamionǁasignar__mutmut['xǁCamionǁasignar__mutmut_13'] = Camion.xǁCamionǁasignar__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCamionǁasignar__mutmut['xǁCamionǁasignar__mutmut_14'] = Camion.xǁCamionǁasignar__mutmut_14 # type: ignore # mutmut generated
mutants_xǁCamionǁasignar__mutmut['xǁCamionǁasignar__mutmut_15'] = Camion.xǁCamionǁasignar__mutmut_15 # type: ignore # mutmut generated

mutants_xǁCamionǁliberar__mutmut['_mutmut_orig'] = Camion.xǁCamionǁliberar__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCamionǁliberar__mutmut['xǁCamionǁliberar__mutmut_1'] = Camion.xǁCamionǁliberar__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCamionǁliberar__mutmut['xǁCamionǁliberar__mutmut_2'] = Camion.xǁCamionǁliberar__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCamionǁliberar__mutmut['xǁCamionǁliberar__mutmut_3'] = Camion.xǁCamionǁliberar__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCamionǁliberar__mutmut['xǁCamionǁliberar__mutmut_4'] = Camion.xǁCamionǁliberar__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCamionǁliberar__mutmut['xǁCamionǁliberar__mutmut_5'] = Camion.xǁCamionǁliberar__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCamionǁliberar__mutmut['xǁCamionǁliberar__mutmut_6'] = Camion.xǁCamionǁliberar__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCamionǁliberar__mutmut['xǁCamionǁliberar__mutmut_7'] = Camion.xǁCamionǁliberar__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCamionǁliberar__mutmut['xǁCamionǁliberar__mutmut_8'] = Camion.xǁCamionǁliberar__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCamionǁliberar__mutmut['xǁCamionǁliberar__mutmut_9'] = Camion.xǁCamionǁliberar__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCamionǁliberar__mutmut['xǁCamionǁliberar__mutmut_10'] = Camion.xǁCamionǁliberar__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCamionǁliberar__mutmut['xǁCamionǁliberar__mutmut_11'] = Camion.xǁCamionǁliberar__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCamionǁliberar__mutmut['xǁCamionǁliberar__mutmut_12'] = Camion.xǁCamionǁliberar__mutmut_12 # type: ignore # mutmut generated
mutants_xǁCamionǁliberar__mutmut['xǁCamionǁliberar__mutmut_13'] = Camion.xǁCamionǁliberar__mutmut_13 # type: ignore # mutmut generated
mutants_xǁCamionǁliberar__mutmut['xǁCamionǁliberar__mutmut_14'] = Camion.xǁCamionǁliberar__mutmut_14 # type: ignore # mutmut generated

mutants_xǁCamionǁcargar__mutmut['_mutmut_orig'] = Camion.xǁCamionǁcargar__mutmut_orig # type: ignore # mutmut generated
mutants_xǁCamionǁcargar__mutmut['xǁCamionǁcargar__mutmut_1'] = Camion.xǁCamionǁcargar__mutmut_1 # type: ignore # mutmut generated
mutants_xǁCamionǁcargar__mutmut['xǁCamionǁcargar__mutmut_2'] = Camion.xǁCamionǁcargar__mutmut_2 # type: ignore # mutmut generated
mutants_xǁCamionǁcargar__mutmut['xǁCamionǁcargar__mutmut_3'] = Camion.xǁCamionǁcargar__mutmut_3 # type: ignore # mutmut generated
mutants_xǁCamionǁcargar__mutmut['xǁCamionǁcargar__mutmut_4'] = Camion.xǁCamionǁcargar__mutmut_4 # type: ignore # mutmut generated
mutants_xǁCamionǁcargar__mutmut['xǁCamionǁcargar__mutmut_5'] = Camion.xǁCamionǁcargar__mutmut_5 # type: ignore # mutmut generated
mutants_xǁCamionǁcargar__mutmut['xǁCamionǁcargar__mutmut_6'] = Camion.xǁCamionǁcargar__mutmut_6 # type: ignore # mutmut generated
mutants_xǁCamionǁcargar__mutmut['xǁCamionǁcargar__mutmut_7'] = Camion.xǁCamionǁcargar__mutmut_7 # type: ignore # mutmut generated
mutants_xǁCamionǁcargar__mutmut['xǁCamionǁcargar__mutmut_8'] = Camion.xǁCamionǁcargar__mutmut_8 # type: ignore # mutmut generated
mutants_xǁCamionǁcargar__mutmut['xǁCamionǁcargar__mutmut_9'] = Camion.xǁCamionǁcargar__mutmut_9 # type: ignore # mutmut generated
mutants_xǁCamionǁcargar__mutmut['xǁCamionǁcargar__mutmut_10'] = Camion.xǁCamionǁcargar__mutmut_10 # type: ignore # mutmut generated
mutants_xǁCamionǁcargar__mutmut['xǁCamionǁcargar__mutmut_11'] = Camion.xǁCamionǁcargar__mutmut_11 # type: ignore # mutmut generated
mutants_xǁCamionǁcargar__mutmut['xǁCamionǁcargar__mutmut_12'] = Camion.xǁCamionǁcargar__mutmut_12 # type: ignore # mutmut generated
