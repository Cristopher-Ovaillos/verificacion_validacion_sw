# Proveniencia: Copiado de Unidad_III/Ejercicio1/flota/servicio_mantenimiento.py
# Original:      Nuevo en Unidad III


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁServicioMantenimientoǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁServicioMantenimientoǁingresar__mutmut: MutantDict = {}  # type: ignore
mutants_xǁServicioMantenimientoǁliberar__mutmut: MutantDict = {}  # type: ignore
class ServicioMantenimiento:
    @_mutmut_mutated(mutants_xǁServicioMantenimientoǁ__init____mutmut)
    def __init__(self, registro_km):
        self._vehiculos_en_taller = []
        self._registro = registro_km
    def xǁServicioMantenimientoǁ__init____mutmut_orig(self, registro_km):
        self._vehiculos_en_taller = []
        self._registro = registro_km
    def xǁServicioMantenimientoǁ__init____mutmut_1(self, registro_km):
        self._vehiculos_en_taller = None
        self._registro = registro_km
    def xǁServicioMantenimientoǁ__init____mutmut_2(self, registro_km):
        self._vehiculos_en_taller = []
        self._registro = None

    @_mutmut_mutated(mutants_xǁServicioMantenimientoǁingresar__mutmut)
    def ingresar(self, vehiculo) -> str:
        if vehiculo.get_estado().name != 'MANTENIMIENTO':
            raise PermissionError('El vehículo debe estar en estado MANTENIMIENTO')
        patente = vehiculo.get_patente()
        self._vehiculos_en_taller.append(patente)
        km_actual = self._registro.obtener_km(patente)
        return f'Vehículo {patente} ingresado al taller. KM actuales: {km_actual}'

    def xǁServicioMantenimientoǁingresar__mutmut_orig(self, vehiculo) -> str:
        if vehiculo.get_estado().name != 'MANTENIMIENTO':
            raise PermissionError('El vehículo debe estar en estado MANTENIMIENTO')
        patente = vehiculo.get_patente()
        self._vehiculos_en_taller.append(patente)
        km_actual = self._registro.obtener_km(patente)
        return f'Vehículo {patente} ingresado al taller. KM actuales: {km_actual}'

    def xǁServicioMantenimientoǁingresar__mutmut_1(self, vehiculo) -> str:
        if vehiculo.get_estado().name == 'MANTENIMIENTO':
            raise PermissionError('El vehículo debe estar en estado MANTENIMIENTO')
        patente = vehiculo.get_patente()
        self._vehiculos_en_taller.append(patente)
        km_actual = self._registro.obtener_km(patente)
        return f'Vehículo {patente} ingresado al taller. KM actuales: {km_actual}'

    def xǁServicioMantenimientoǁingresar__mutmut_2(self, vehiculo) -> str:
        if vehiculo.get_estado().name != 'XXMANTENIMIENTOXX':
            raise PermissionError('El vehículo debe estar en estado MANTENIMIENTO')
        patente = vehiculo.get_patente()
        self._vehiculos_en_taller.append(patente)
        km_actual = self._registro.obtener_km(patente)
        return f'Vehículo {patente} ingresado al taller. KM actuales: {km_actual}'

    def xǁServicioMantenimientoǁingresar__mutmut_3(self, vehiculo) -> str:
        if vehiculo.get_estado().name != 'mantenimiento':
            raise PermissionError('El vehículo debe estar en estado MANTENIMIENTO')
        patente = vehiculo.get_patente()
        self._vehiculos_en_taller.append(patente)
        km_actual = self._registro.obtener_km(patente)
        return f'Vehículo {patente} ingresado al taller. KM actuales: {km_actual}'

    def xǁServicioMantenimientoǁingresar__mutmut_4(self, vehiculo) -> str:
        if vehiculo.get_estado().name != 'MANTENIMIENTO':
            raise PermissionError(None)
        patente = vehiculo.get_patente()
        self._vehiculos_en_taller.append(patente)
        km_actual = self._registro.obtener_km(patente)
        return f'Vehículo {patente} ingresado al taller. KM actuales: {km_actual}'

    def xǁServicioMantenimientoǁingresar__mutmut_5(self, vehiculo) -> str:
        if vehiculo.get_estado().name != 'MANTENIMIENTO':
            raise PermissionError('XXEl vehículo debe estar en estado MANTENIMIENTOXX')
        patente = vehiculo.get_patente()
        self._vehiculos_en_taller.append(patente)
        km_actual = self._registro.obtener_km(patente)
        return f'Vehículo {patente} ingresado al taller. KM actuales: {km_actual}'

    def xǁServicioMantenimientoǁingresar__mutmut_6(self, vehiculo) -> str:
        if vehiculo.get_estado().name != 'MANTENIMIENTO':
            raise PermissionError('el vehículo debe estar en estado mantenimiento')
        patente = vehiculo.get_patente()
        self._vehiculos_en_taller.append(patente)
        km_actual = self._registro.obtener_km(patente)
        return f'Vehículo {patente} ingresado al taller. KM actuales: {km_actual}'

    def xǁServicioMantenimientoǁingresar__mutmut_7(self, vehiculo) -> str:
        if vehiculo.get_estado().name != 'MANTENIMIENTO':
            raise PermissionError('EL VEHÍCULO DEBE ESTAR EN ESTADO MANTENIMIENTO')
        patente = vehiculo.get_patente()
        self._vehiculos_en_taller.append(patente)
        km_actual = self._registro.obtener_km(patente)
        return f'Vehículo {patente} ingresado al taller. KM actuales: {km_actual}'

    def xǁServicioMantenimientoǁingresar__mutmut_8(self, vehiculo) -> str:
        if vehiculo.get_estado().name != 'MANTENIMIENTO':
            raise PermissionError('El vehículo debe estar en estado MANTENIMIENTO')
        patente = None
        self._vehiculos_en_taller.append(patente)
        km_actual = self._registro.obtener_km(patente)
        return f'Vehículo {patente} ingresado al taller. KM actuales: {km_actual}'

    def xǁServicioMantenimientoǁingresar__mutmut_9(self, vehiculo) -> str:
        if vehiculo.get_estado().name != 'MANTENIMIENTO':
            raise PermissionError('El vehículo debe estar en estado MANTENIMIENTO')
        patente = vehiculo.get_patente()
        self._vehiculos_en_taller.append(None)
        km_actual = self._registro.obtener_km(patente)
        return f'Vehículo {patente} ingresado al taller. KM actuales: {km_actual}'

    def xǁServicioMantenimientoǁingresar__mutmut_10(self, vehiculo) -> str:
        if vehiculo.get_estado().name != 'MANTENIMIENTO':
            raise PermissionError('El vehículo debe estar en estado MANTENIMIENTO')
        patente = vehiculo.get_patente()
        self._vehiculos_en_taller.append(patente)
        km_actual = None
        return f'Vehículo {patente} ingresado al taller. KM actuales: {km_actual}'

    def xǁServicioMantenimientoǁingresar__mutmut_11(self, vehiculo) -> str:
        if vehiculo.get_estado().name != 'MANTENIMIENTO':
            raise PermissionError('El vehículo debe estar en estado MANTENIMIENTO')
        patente = vehiculo.get_patente()
        self._vehiculos_en_taller.append(patente)
        km_actual = self._registro.obtener_km(None)
        return f'Vehículo {patente} ingresado al taller. KM actuales: {km_actual}'

    @_mutmut_mutated(mutants_xǁServicioMantenimientoǁliberar__mutmut)
    def liberar(self, vehiculo) -> None:
        patente = vehiculo.get_patente()
        if patente not in self._vehiculos_en_taller:
            raise KeyError('Vehículo no está en el taller')
        self._vehiculos_en_taller.remove(patente)
        # BUG intencional: debería ser vehiculo.liberar(0) o similar
        vehiculo.enviar_mantenimiento()

    def xǁServicioMantenimientoǁliberar__mutmut_orig(self, vehiculo) -> None:
        patente = vehiculo.get_patente()
        if patente not in self._vehiculos_en_taller:
            raise KeyError('Vehículo no está en el taller')
        self._vehiculos_en_taller.remove(patente)
        # BUG intencional: debería ser vehiculo.liberar(0) o similar
        vehiculo.enviar_mantenimiento()

    def xǁServicioMantenimientoǁliberar__mutmut_1(self, vehiculo) -> None:
        patente = None
        if patente not in self._vehiculos_en_taller:
            raise KeyError('Vehículo no está en el taller')
        self._vehiculos_en_taller.remove(patente)
        # BUG intencional: debería ser vehiculo.liberar(0) o similar
        vehiculo.enviar_mantenimiento()

    def xǁServicioMantenimientoǁliberar__mutmut_2(self, vehiculo) -> None:
        patente = vehiculo.get_patente()
        if patente in self._vehiculos_en_taller:
            raise KeyError('Vehículo no está en el taller')
        self._vehiculos_en_taller.remove(patente)
        # BUG intencional: debería ser vehiculo.liberar(0) o similar
        vehiculo.enviar_mantenimiento()

    def xǁServicioMantenimientoǁliberar__mutmut_3(self, vehiculo) -> None:
        patente = vehiculo.get_patente()
        if patente not in self._vehiculos_en_taller:
            raise KeyError(None)
        self._vehiculos_en_taller.remove(patente)
        # BUG intencional: debería ser vehiculo.liberar(0) o similar
        vehiculo.enviar_mantenimiento()

    def xǁServicioMantenimientoǁliberar__mutmut_4(self, vehiculo) -> None:
        patente = vehiculo.get_patente()
        if patente not in self._vehiculos_en_taller:
            raise KeyError('XXVehículo no está en el tallerXX')
        self._vehiculos_en_taller.remove(patente)
        # BUG intencional: debería ser vehiculo.liberar(0) o similar
        vehiculo.enviar_mantenimiento()

    def xǁServicioMantenimientoǁliberar__mutmut_5(self, vehiculo) -> None:
        patente = vehiculo.get_patente()
        if patente not in self._vehiculos_en_taller:
            raise KeyError('vehículo no está en el taller')
        self._vehiculos_en_taller.remove(patente)
        # BUG intencional: debería ser vehiculo.liberar(0) o similar
        vehiculo.enviar_mantenimiento()

    def xǁServicioMantenimientoǁliberar__mutmut_6(self, vehiculo) -> None:
        patente = vehiculo.get_patente()
        if patente not in self._vehiculos_en_taller:
            raise KeyError('VEHÍCULO NO ESTÁ EN EL TALLER')
        self._vehiculos_en_taller.remove(patente)
        # BUG intencional: debería ser vehiculo.liberar(0) o similar
        vehiculo.enviar_mantenimiento()

    def xǁServicioMantenimientoǁliberar__mutmut_7(self, vehiculo) -> None:
        patente = vehiculo.get_patente()
        if patente not in self._vehiculos_en_taller:
            raise KeyError('Vehículo no está en el taller')
        self._vehiculos_en_taller.remove(None)
        # BUG intencional: debería ser vehiculo.liberar(0) o similar
        vehiculo.enviar_mantenimiento()

mutants_xǁServicioMantenimientoǁ__init____mutmut['_mutmut_orig'] = ServicioMantenimiento.xǁServicioMantenimientoǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁ__init____mutmut['xǁServicioMantenimientoǁ__init____mutmut_1'] = ServicioMantenimiento.xǁServicioMantenimientoǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁ__init____mutmut['xǁServicioMantenimientoǁ__init____mutmut_2'] = ServicioMantenimiento.xǁServicioMantenimientoǁ__init____mutmut_2 # type: ignore # mutmut generated

mutants_xǁServicioMantenimientoǁingresar__mutmut['_mutmut_orig'] = ServicioMantenimiento.xǁServicioMantenimientoǁingresar__mutmut_orig # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁingresar__mutmut['xǁServicioMantenimientoǁingresar__mutmut_1'] = ServicioMantenimiento.xǁServicioMantenimientoǁingresar__mutmut_1 # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁingresar__mutmut['xǁServicioMantenimientoǁingresar__mutmut_2'] = ServicioMantenimiento.xǁServicioMantenimientoǁingresar__mutmut_2 # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁingresar__mutmut['xǁServicioMantenimientoǁingresar__mutmut_3'] = ServicioMantenimiento.xǁServicioMantenimientoǁingresar__mutmut_3 # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁingresar__mutmut['xǁServicioMantenimientoǁingresar__mutmut_4'] = ServicioMantenimiento.xǁServicioMantenimientoǁingresar__mutmut_4 # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁingresar__mutmut['xǁServicioMantenimientoǁingresar__mutmut_5'] = ServicioMantenimiento.xǁServicioMantenimientoǁingresar__mutmut_5 # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁingresar__mutmut['xǁServicioMantenimientoǁingresar__mutmut_6'] = ServicioMantenimiento.xǁServicioMantenimientoǁingresar__mutmut_6 # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁingresar__mutmut['xǁServicioMantenimientoǁingresar__mutmut_7'] = ServicioMantenimiento.xǁServicioMantenimientoǁingresar__mutmut_7 # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁingresar__mutmut['xǁServicioMantenimientoǁingresar__mutmut_8'] = ServicioMantenimiento.xǁServicioMantenimientoǁingresar__mutmut_8 # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁingresar__mutmut['xǁServicioMantenimientoǁingresar__mutmut_9'] = ServicioMantenimiento.xǁServicioMantenimientoǁingresar__mutmut_9 # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁingresar__mutmut['xǁServicioMantenimientoǁingresar__mutmut_10'] = ServicioMantenimiento.xǁServicioMantenimientoǁingresar__mutmut_10 # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁingresar__mutmut['xǁServicioMantenimientoǁingresar__mutmut_11'] = ServicioMantenimiento.xǁServicioMantenimientoǁingresar__mutmut_11 # type: ignore # mutmut generated

mutants_xǁServicioMantenimientoǁliberar__mutmut['_mutmut_orig'] = ServicioMantenimiento.xǁServicioMantenimientoǁliberar__mutmut_orig # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁliberar__mutmut['xǁServicioMantenimientoǁliberar__mutmut_1'] = ServicioMantenimiento.xǁServicioMantenimientoǁliberar__mutmut_1 # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁliberar__mutmut['xǁServicioMantenimientoǁliberar__mutmut_2'] = ServicioMantenimiento.xǁServicioMantenimientoǁliberar__mutmut_2 # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁliberar__mutmut['xǁServicioMantenimientoǁliberar__mutmut_3'] = ServicioMantenimiento.xǁServicioMantenimientoǁliberar__mutmut_3 # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁliberar__mutmut['xǁServicioMantenimientoǁliberar__mutmut_4'] = ServicioMantenimiento.xǁServicioMantenimientoǁliberar__mutmut_4 # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁliberar__mutmut['xǁServicioMantenimientoǁliberar__mutmut_5'] = ServicioMantenimiento.xǁServicioMantenimientoǁliberar__mutmut_5 # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁliberar__mutmut['xǁServicioMantenimientoǁliberar__mutmut_6'] = ServicioMantenimiento.xǁServicioMantenimientoǁliberar__mutmut_6 # type: ignore # mutmut generated
mutants_xǁServicioMantenimientoǁliberar__mutmut['xǁServicioMantenimientoǁliberar__mutmut_7'] = ServicioMantenimiento.xǁServicioMantenimientoǁliberar__mutmut_7 # type: ignore # mutmut generated
