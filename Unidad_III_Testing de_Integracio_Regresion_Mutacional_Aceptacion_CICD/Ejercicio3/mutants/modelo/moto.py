# Proveniencia: Copiado de Unidad_III/Ejercicio2/modelo/moto.py
# Original:      Creado en Ejercicio 2 (nueva subclase Vehiculo)
from modelo.auto import EstadoVehiculo


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁMotoǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁMotoǁasignar__mutmut: MutantDict = {}  # type: ignore
mutants_xǁMotoǁliberar__mutmut: MutantDict = {}  # type: ignore


class Moto:
    @_mutmut_mutated(mutants_xǁMotoǁ__init____mutmut)
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
    def xǁMotoǁ__init____mutmut_orig(self, patente: str, marca: str, anio: int,
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
    def xǁMotoǁ__init____mutmut_1(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente and len(patente) < 6:
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
    def xǁMotoǁ__init____mutmut_2(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if patente or len(patente) < 6:
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
    def xǁMotoǁ__init____mutmut_3(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) <= 6:
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
    def xǁMotoǁ__init____mutmut_4(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) < 7:
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
    def xǁMotoǁ__init____mutmut_5(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) < 6:
            raise ValueError(None)
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
    def xǁMotoǁ__init____mutmut_6(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) < 6:
            raise ValueError('XXPatente inválidaXX')
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
    def xǁMotoǁ__init____mutmut_7(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) < 6:
            raise ValueError('patente inválida')
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
    def xǁMotoǁ__init____mutmut_8(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) < 6:
            raise ValueError('PATENTE INVÁLIDA')
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
    def xǁMotoǁ__init____mutmut_9(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales <= 0:
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
    def xǁMotoǁ__init____mutmut_10(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 1:
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
    def xǁMotoǁ__init____mutmut_11(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError(None)
        if cilindrada <= 0:
            raise ValueError('cilindrada debe ser positiva')
        self._patente    = patente
        self._marca      = marca
        self._anio       = anio
        self._km         = km_actuales
        self._cilindrada = cilindrada
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None
    def xǁMotoǁ__init____mutmut_12(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('XXkm_actuales no puede ser negativoXX')
        if cilindrada <= 0:
            raise ValueError('cilindrada debe ser positiva')
        self._patente    = patente
        self._marca      = marca
        self._anio       = anio
        self._km         = km_actuales
        self._cilindrada = cilindrada
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None
    def xǁMotoǁ__init____mutmut_13(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('KM_ACTUALES NO PUEDE SER NEGATIVO')
        if cilindrada <= 0:
            raise ValueError('cilindrada debe ser positiva')
        self._patente    = patente
        self._marca      = marca
        self._anio       = anio
        self._km         = km_actuales
        self._cilindrada = cilindrada
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None
    def xǁMotoǁ__init____mutmut_14(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('km_actuales no puede ser negativo')
        if cilindrada < 0:
            raise ValueError('cilindrada debe ser positiva')
        self._patente    = patente
        self._marca      = marca
        self._anio       = anio
        self._km         = km_actuales
        self._cilindrada = cilindrada
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None
    def xǁMotoǁ__init____mutmut_15(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('km_actuales no puede ser negativo')
        if cilindrada <= 1:
            raise ValueError('cilindrada debe ser positiva')
        self._patente    = patente
        self._marca      = marca
        self._anio       = anio
        self._km         = km_actuales
        self._cilindrada = cilindrada
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None
    def xǁMotoǁ__init____mutmut_16(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('km_actuales no puede ser negativo')
        if cilindrada <= 0:
            raise ValueError(None)
        self._patente    = patente
        self._marca      = marca
        self._anio       = anio
        self._km         = km_actuales
        self._cilindrada = cilindrada
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None
    def xǁMotoǁ__init____mutmut_17(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('km_actuales no puede ser negativo')
        if cilindrada <= 0:
            raise ValueError('XXcilindrada debe ser positivaXX')
        self._patente    = patente
        self._marca      = marca
        self._anio       = anio
        self._km         = km_actuales
        self._cilindrada = cilindrada
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None
    def xǁMotoǁ__init____mutmut_18(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('km_actuales no puede ser negativo')
        if cilindrada <= 0:
            raise ValueError('CILINDRADA DEBE SER POSITIVA')
        self._patente    = patente
        self._marca      = marca
        self._anio       = anio
        self._km         = km_actuales
        self._cilindrada = cilindrada
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None
    def xǁMotoǁ__init____mutmut_19(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('km_actuales no puede ser negativo')
        if cilindrada <= 0:
            raise ValueError('cilindrada debe ser positiva')
        self._patente    = None
        self._marca      = marca
        self._anio       = anio
        self._km         = km_actuales
        self._cilindrada = cilindrada
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None
    def xǁMotoǁ__init____mutmut_20(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('km_actuales no puede ser negativo')
        if cilindrada <= 0:
            raise ValueError('cilindrada debe ser positiva')
        self._patente    = patente
        self._marca      = None
        self._anio       = anio
        self._km         = km_actuales
        self._cilindrada = cilindrada
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None
    def xǁMotoǁ__init____mutmut_21(self, patente: str, marca: str, anio: int,
                 km_actuales: float, cilindrada: int):
        if not patente or len(patente) < 6:
            raise ValueError('Patente inválida')
        if km_actuales < 0:
            raise ValueError('km_actuales no puede ser negativo')
        if cilindrada <= 0:
            raise ValueError('cilindrada debe ser positiva')
        self._patente    = patente
        self._marca      = marca
        self._anio       = None
        self._km         = km_actuales
        self._cilindrada = cilindrada
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None
    def xǁMotoǁ__init____mutmut_22(self, patente: str, marca: str, anio: int,
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
        self._km         = None
        self._cilindrada = cilindrada
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None
    def xǁMotoǁ__init____mutmut_23(self, patente: str, marca: str, anio: int,
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
        self._cilindrada = None
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None
    def xǁMotoǁ__init____mutmut_24(self, patente: str, marca: str, anio: int,
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
        self._estado     = None
        self._conductor  = None
    def xǁMotoǁ__init____mutmut_25(self, patente: str, marca: str, anio: int,
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
        self._conductor  = ""

    @_mutmut_mutated(mutants_xǁMotoǁasignar__mutmut)
    def asignar(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,300]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 300:
            raise ValueError('km_estimados fuera de rango para moto')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Moto {self._patente} asignada a {legajo_conductor} por {km_estimados} km'

    def xǁMotoǁasignar__mutmut_orig(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,300]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 300:
            raise ValueError('km_estimados fuera de rango para moto')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Moto {self._patente} asignada a {legajo_conductor} por {km_estimados} km'

    def xǁMotoǁasignar__mutmut_1(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,300]."""
        if self._estado == EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 300:
            raise ValueError('km_estimados fuera de rango para moto')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Moto {self._patente} asignada a {legajo_conductor} por {km_estimados} km'

    def xǁMotoǁasignar__mutmut_2(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,300]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError(None)
        if km_estimados <= 0 or km_estimados > 300:
            raise ValueError('km_estimados fuera de rango para moto')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Moto {self._patente} asignada a {legajo_conductor} por {km_estimados} km'

    def xǁMotoǁasignar__mutmut_3(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,300]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('XXVehículo no disponibleXX')
        if km_estimados <= 0 or km_estimados > 300:
            raise ValueError('km_estimados fuera de rango para moto')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Moto {self._patente} asignada a {legajo_conductor} por {km_estimados} km'

    def xǁMotoǁasignar__mutmut_4(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,300]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 300:
            raise ValueError('km_estimados fuera de rango para moto')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Moto {self._patente} asignada a {legajo_conductor} por {km_estimados} km'

    def xǁMotoǁasignar__mutmut_5(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,300]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('VEHÍCULO NO DISPONIBLE')
        if km_estimados <= 0 or km_estimados > 300:
            raise ValueError('km_estimados fuera de rango para moto')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Moto {self._patente} asignada a {legajo_conductor} por {km_estimados} km'

    def xǁMotoǁasignar__mutmut_6(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,300]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 and km_estimados > 300:
            raise ValueError('km_estimados fuera de rango para moto')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Moto {self._patente} asignada a {legajo_conductor} por {km_estimados} km'

    def xǁMotoǁasignar__mutmut_7(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,300]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados < 0 or km_estimados > 300:
            raise ValueError('km_estimados fuera de rango para moto')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Moto {self._patente} asignada a {legajo_conductor} por {km_estimados} km'

    def xǁMotoǁasignar__mutmut_8(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,300]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 1 or km_estimados > 300:
            raise ValueError('km_estimados fuera de rango para moto')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Moto {self._patente} asignada a {legajo_conductor} por {km_estimados} km'

    def xǁMotoǁasignar__mutmut_9(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,300]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados >= 300:
            raise ValueError('km_estimados fuera de rango para moto')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Moto {self._patente} asignada a {legajo_conductor} por {km_estimados} km'

    def xǁMotoǁasignar__mutmut_10(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,300]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 301:
            raise ValueError('km_estimados fuera de rango para moto')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Moto {self._patente} asignada a {legajo_conductor} por {km_estimados} km'

    def xǁMotoǁasignar__mutmut_11(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,300]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 300:
            raise ValueError(None)
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Moto {self._patente} asignada a {legajo_conductor} por {km_estimados} km'

    def xǁMotoǁasignar__mutmut_12(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,300]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 300:
            raise ValueError('XXkm_estimados fuera de rango para motoXX')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Moto {self._patente} asignada a {legajo_conductor} por {km_estimados} km'

    def xǁMotoǁasignar__mutmut_13(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,300]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 300:
            raise ValueError('KM_ESTIMADOS FUERA DE RANGO PARA MOTO')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = legajo_conductor
        return f'Moto {self._patente} asignada a {legajo_conductor} por {km_estimados} km'

    def xǁMotoǁasignar__mutmut_14(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,300]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 300:
            raise ValueError('km_estimados fuera de rango para moto')
        self._estado    = None
        self._conductor = legajo_conductor
        return f'Moto {self._patente} asignada a {legajo_conductor} por {km_estimados} km'

    def xǁMotoǁasignar__mutmut_15(self, legajo_conductor: str, km_estimados: float) -> str:
        """Pre: estado=DISPONIBLE, km_estimados in (0,300]."""
        if self._estado != EstadoVehiculo.DISPONIBLE:
            raise PermissionError('Vehículo no disponible')
        if km_estimados <= 0 or km_estimados > 300:
            raise ValueError('km_estimados fuera de rango para moto')
        self._estado    = EstadoVehiculo.EN_USO
        self._conductor = None
        return f'Moto {self._patente} asignada a {legajo_conductor} por {km_estimados} km'

    @_mutmut_mutated(mutants_xǁMotoǁliberar__mutmut)
    def liberar(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('La moto no está en uso')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁMotoǁliberar__mutmut_orig(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('La moto no está en uso')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁMotoǁliberar__mutmut_1(self, km_recorridos: float) -> None:
        if self._estado == EstadoVehiculo.EN_USO:
            raise PermissionError('La moto no está en uso')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁMotoǁliberar__mutmut_2(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError(None)
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁMotoǁliberar__mutmut_3(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('XXLa moto no está en usoXX')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁMotoǁliberar__mutmut_4(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('la moto no está en uso')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁMotoǁliberar__mutmut_5(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('LA MOTO NO ESTÁ EN USO')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁMotoǁliberar__mutmut_6(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('La moto no está en uso')
        if km_recorridos <= 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁMotoǁliberar__mutmut_7(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('La moto no está en uso')
        if km_recorridos < 1:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁMotoǁliberar__mutmut_8(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('La moto no está en uso')
        if km_recorridos < 0:
            raise ValueError(None)
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁMotoǁliberar__mutmut_9(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('La moto no está en uso')
        if km_recorridos < 0:
            raise ValueError('XXkm_recorridos no puede ser negativoXX')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁMotoǁliberar__mutmut_10(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('La moto no está en uso')
        if km_recorridos < 0:
            raise ValueError('KM_RECORRIDOS NO PUEDE SER NEGATIVO')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁMotoǁliberar__mutmut_11(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('La moto no está en uso')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km = km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁMotoǁliberar__mutmut_12(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('La moto no está en uso')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km -= km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = None

    def xǁMotoǁliberar__mutmut_13(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('La moto no está en uso')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = None
        self._conductor  = None

    def xǁMotoǁliberar__mutmut_14(self, km_recorridos: float) -> None:
        if self._estado != EstadoVehiculo.EN_USO:
            raise PermissionError('La moto no está en uso')
        if km_recorridos < 0:
            raise ValueError('km_recorridos no puede ser negativo')
        self._km        += km_recorridos
        self._estado     = EstadoVehiculo.DISPONIBLE
        self._conductor  = ""

    def get_estado(self) -> EstadoVehiculo:
        return self._estado

    def get_km(self) -> float:
        return self._km

    def get_patente(self) -> str:
        return self._patente

    def get_conductor(self):
        return self._conductor

mutants_xǁMotoǁ__init____mutmut['_mutmut_orig'] = Moto.xǁMotoǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_1'] = Moto.xǁMotoǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_2'] = Moto.xǁMotoǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_3'] = Moto.xǁMotoǁ__init____mutmut_3 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_4'] = Moto.xǁMotoǁ__init____mutmut_4 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_5'] = Moto.xǁMotoǁ__init____mutmut_5 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_6'] = Moto.xǁMotoǁ__init____mutmut_6 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_7'] = Moto.xǁMotoǁ__init____mutmut_7 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_8'] = Moto.xǁMotoǁ__init____mutmut_8 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_9'] = Moto.xǁMotoǁ__init____mutmut_9 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_10'] = Moto.xǁMotoǁ__init____mutmut_10 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_11'] = Moto.xǁMotoǁ__init____mutmut_11 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_12'] = Moto.xǁMotoǁ__init____mutmut_12 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_13'] = Moto.xǁMotoǁ__init____mutmut_13 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_14'] = Moto.xǁMotoǁ__init____mutmut_14 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_15'] = Moto.xǁMotoǁ__init____mutmut_15 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_16'] = Moto.xǁMotoǁ__init____mutmut_16 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_17'] = Moto.xǁMotoǁ__init____mutmut_17 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_18'] = Moto.xǁMotoǁ__init____mutmut_18 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_19'] = Moto.xǁMotoǁ__init____mutmut_19 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_20'] = Moto.xǁMotoǁ__init____mutmut_20 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_21'] = Moto.xǁMotoǁ__init____mutmut_21 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_22'] = Moto.xǁMotoǁ__init____mutmut_22 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_23'] = Moto.xǁMotoǁ__init____mutmut_23 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_24'] = Moto.xǁMotoǁ__init____mutmut_24 # type: ignore # mutmut generated
mutants_xǁMotoǁ__init____mutmut['xǁMotoǁ__init____mutmut_25'] = Moto.xǁMotoǁ__init____mutmut_25 # type: ignore # mutmut generated

mutants_xǁMotoǁasignar__mutmut['_mutmut_orig'] = Moto.xǁMotoǁasignar__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMotoǁasignar__mutmut['xǁMotoǁasignar__mutmut_1'] = Moto.xǁMotoǁasignar__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMotoǁasignar__mutmut['xǁMotoǁasignar__mutmut_2'] = Moto.xǁMotoǁasignar__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMotoǁasignar__mutmut['xǁMotoǁasignar__mutmut_3'] = Moto.xǁMotoǁasignar__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMotoǁasignar__mutmut['xǁMotoǁasignar__mutmut_4'] = Moto.xǁMotoǁasignar__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMotoǁasignar__mutmut['xǁMotoǁasignar__mutmut_5'] = Moto.xǁMotoǁasignar__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMotoǁasignar__mutmut['xǁMotoǁasignar__mutmut_6'] = Moto.xǁMotoǁasignar__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMotoǁasignar__mutmut['xǁMotoǁasignar__mutmut_7'] = Moto.xǁMotoǁasignar__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMotoǁasignar__mutmut['xǁMotoǁasignar__mutmut_8'] = Moto.xǁMotoǁasignar__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMotoǁasignar__mutmut['xǁMotoǁasignar__mutmut_9'] = Moto.xǁMotoǁasignar__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMotoǁasignar__mutmut['xǁMotoǁasignar__mutmut_10'] = Moto.xǁMotoǁasignar__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMotoǁasignar__mutmut['xǁMotoǁasignar__mutmut_11'] = Moto.xǁMotoǁasignar__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMotoǁasignar__mutmut['xǁMotoǁasignar__mutmut_12'] = Moto.xǁMotoǁasignar__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMotoǁasignar__mutmut['xǁMotoǁasignar__mutmut_13'] = Moto.xǁMotoǁasignar__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMotoǁasignar__mutmut['xǁMotoǁasignar__mutmut_14'] = Moto.xǁMotoǁasignar__mutmut_14 # type: ignore # mutmut generated
mutants_xǁMotoǁasignar__mutmut['xǁMotoǁasignar__mutmut_15'] = Moto.xǁMotoǁasignar__mutmut_15 # type: ignore # mutmut generated

mutants_xǁMotoǁliberar__mutmut['_mutmut_orig'] = Moto.xǁMotoǁliberar__mutmut_orig # type: ignore # mutmut generated
mutants_xǁMotoǁliberar__mutmut['xǁMotoǁliberar__mutmut_1'] = Moto.xǁMotoǁliberar__mutmut_1 # type: ignore # mutmut generated
mutants_xǁMotoǁliberar__mutmut['xǁMotoǁliberar__mutmut_2'] = Moto.xǁMotoǁliberar__mutmut_2 # type: ignore # mutmut generated
mutants_xǁMotoǁliberar__mutmut['xǁMotoǁliberar__mutmut_3'] = Moto.xǁMotoǁliberar__mutmut_3 # type: ignore # mutmut generated
mutants_xǁMotoǁliberar__mutmut['xǁMotoǁliberar__mutmut_4'] = Moto.xǁMotoǁliberar__mutmut_4 # type: ignore # mutmut generated
mutants_xǁMotoǁliberar__mutmut['xǁMotoǁliberar__mutmut_5'] = Moto.xǁMotoǁliberar__mutmut_5 # type: ignore # mutmut generated
mutants_xǁMotoǁliberar__mutmut['xǁMotoǁliberar__mutmut_6'] = Moto.xǁMotoǁliberar__mutmut_6 # type: ignore # mutmut generated
mutants_xǁMotoǁliberar__mutmut['xǁMotoǁliberar__mutmut_7'] = Moto.xǁMotoǁliberar__mutmut_7 # type: ignore # mutmut generated
mutants_xǁMotoǁliberar__mutmut['xǁMotoǁliberar__mutmut_8'] = Moto.xǁMotoǁliberar__mutmut_8 # type: ignore # mutmut generated
mutants_xǁMotoǁliberar__mutmut['xǁMotoǁliberar__mutmut_9'] = Moto.xǁMotoǁliberar__mutmut_9 # type: ignore # mutmut generated
mutants_xǁMotoǁliberar__mutmut['xǁMotoǁliberar__mutmut_10'] = Moto.xǁMotoǁliberar__mutmut_10 # type: ignore # mutmut generated
mutants_xǁMotoǁliberar__mutmut['xǁMotoǁliberar__mutmut_11'] = Moto.xǁMotoǁliberar__mutmut_11 # type: ignore # mutmut generated
mutants_xǁMotoǁliberar__mutmut['xǁMotoǁliberar__mutmut_12'] = Moto.xǁMotoǁliberar__mutmut_12 # type: ignore # mutmut generated
mutants_xǁMotoǁliberar__mutmut['xǁMotoǁliberar__mutmut_13'] = Moto.xǁMotoǁliberar__mutmut_13 # type: ignore # mutmut generated
mutants_xǁMotoǁliberar__mutmut['xǁMotoǁliberar__mutmut_14'] = Moto.xǁMotoǁliberar__mutmut_14 # type: ignore # mutmut generated
