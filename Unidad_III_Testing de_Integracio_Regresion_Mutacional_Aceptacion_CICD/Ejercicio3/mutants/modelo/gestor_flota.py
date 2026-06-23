# Proveniencia: Copiado de Unidad_III/Ejercicio2/modelo/gestor_flota.py
# Original:      Unidad_II/flota/gestor_flota.py + ValidadorLegajo (Cambio C)
import threading


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁValidadorLegajoǁvalidar__mutmut: MutantDict = {}  # type: ignore

class ValidadorLegajo:
    @_mutmut_mutated(mutants_xǁValidadorLegajoǁvalidar__mutmut)
    def validar(self, legajo: str) -> bool:
        if not legajo or len(legajo) < 4:
            return False
        return True
    def xǁValidadorLegajoǁvalidar__mutmut_orig(self, legajo: str) -> bool:
        if not legajo or len(legajo) < 4:
            return False
        return True
    def xǁValidadorLegajoǁvalidar__mutmut_1(self, legajo: str) -> bool:
        if not legajo and len(legajo) < 4:
            return False
        return True
    def xǁValidadorLegajoǁvalidar__mutmut_2(self, legajo: str) -> bool:
        if legajo or len(legajo) < 4:
            return False
        return True
    def xǁValidadorLegajoǁvalidar__mutmut_3(self, legajo: str) -> bool:
        if not legajo or len(legajo) <= 4:
            return False
        return True
    def xǁValidadorLegajoǁvalidar__mutmut_4(self, legajo: str) -> bool:
        if not legajo or len(legajo) < 5:
            return False
        return True
    def xǁValidadorLegajoǁvalidar__mutmut_5(self, legajo: str) -> bool:
        if not legajo or len(legajo) < 4:
            return True
        return True
    def xǁValidadorLegajoǁvalidar__mutmut_6(self, legajo: str) -> bool:
        if not legajo or len(legajo) < 4:
            return False
        return False

mutants_xǁValidadorLegajoǁvalidar__mutmut['_mutmut_orig'] = ValidadorLegajo.xǁValidadorLegajoǁvalidar__mutmut_orig # type: ignore # mutmut generated
mutants_xǁValidadorLegajoǁvalidar__mutmut['xǁValidadorLegajoǁvalidar__mutmut_1'] = ValidadorLegajo.xǁValidadorLegajoǁvalidar__mutmut_1 # type: ignore # mutmut generated
mutants_xǁValidadorLegajoǁvalidar__mutmut['xǁValidadorLegajoǁvalidar__mutmut_2'] = ValidadorLegajo.xǁValidadorLegajoǁvalidar__mutmut_2 # type: ignore # mutmut generated
mutants_xǁValidadorLegajoǁvalidar__mutmut['xǁValidadorLegajoǁvalidar__mutmut_3'] = ValidadorLegajo.xǁValidadorLegajoǁvalidar__mutmut_3 # type: ignore # mutmut generated
mutants_xǁValidadorLegajoǁvalidar__mutmut['xǁValidadorLegajoǁvalidar__mutmut_4'] = ValidadorLegajo.xǁValidadorLegajoǁvalidar__mutmut_4 # type: ignore # mutmut generated
mutants_xǁValidadorLegajoǁvalidar__mutmut['xǁValidadorLegajoǁvalidar__mutmut_5'] = ValidadorLegajo.xǁValidadorLegajoǁvalidar__mutmut_5 # type: ignore # mutmut generated
mutants_xǁValidadorLegajoǁvalidar__mutmut['xǁValidadorLegajoǁvalidar__mutmut_6'] = ValidadorLegajo.xǁValidadorLegajoǁvalidar__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁGestorFlotaǁget_instancia__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGestorFlotaǁregistrar__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGestorFlotaǁasignar__mutmut: MutantDict = {}  # type: ignore
mutants_xǁGestorFlotaǁ_reset_para_tests__mutmut: MutantDict = {}  # type: ignore

class GestorFlota:
    _instancia = None
    _lock = threading.Lock()

    @_mutmut_mutated(mutants_xǁGestorFlotaǁ__init____mutmut)
    def __init__(self):
        self._vehiculos = {}
        self._asignaciones = 0

    def xǁGestorFlotaǁ__init____mutmut_orig(self):
        self._vehiculos = {}
        self._asignaciones = 0

    def xǁGestorFlotaǁ__init____mutmut_1(self):
        self._vehiculos = None
        self._asignaciones = 0

    def xǁGestorFlotaǁ__init____mutmut_2(self):
        self._vehiculos = {}
        self._asignaciones = None

    def xǁGestorFlotaǁ__init____mutmut_3(self):
        self._vehiculos = {}
        self._asignaciones = 1

    @classmethod
    @_mutmut_mutated(mutants_xǁGestorFlotaǁget_instancia__mutmut, is_classmethod = True)
    def get_instancia(cls):
        if cls._instancia is None:
            with cls._lock:
                if cls._instancia is None:
                    cls._instancia = cls()
        return cls._instancia

    @classmethod
    def xǁGestorFlotaǁget_instancia__mutmut_orig(cls):
        if cls._instancia is None:
            with cls._lock:
                if cls._instancia is None:
                    cls._instancia = cls()
        return cls._instancia

    @classmethod
    def xǁGestorFlotaǁget_instancia__mutmut_1(cls):
        if cls._instancia is not None:
            with cls._lock:
                if cls._instancia is None:
                    cls._instancia = cls()
        return cls._instancia

    @classmethod
    def xǁGestorFlotaǁget_instancia__mutmut_2(cls):
        if cls._instancia is None:
            with cls._lock:
                if cls._instancia is not None:
                    cls._instancia = cls()
        return cls._instancia

    @classmethod
    def xǁGestorFlotaǁget_instancia__mutmut_3(cls):
        if cls._instancia is None:
            with cls._lock:
                if cls._instancia is None:
                    cls._instancia = None
        return cls._instancia

    @_mutmut_mutated(mutants_xǁGestorFlotaǁregistrar__mutmut)
    def registrar(self, vehiculo) -> None:
        if vehiculo.get_patente() in self._vehiculos:
            raise ValueError('Patente ya registrada')
        self._vehiculos[vehiculo.get_patente()] = vehiculo

    def xǁGestorFlotaǁregistrar__mutmut_orig(self, vehiculo) -> None:
        if vehiculo.get_patente() in self._vehiculos:
            raise ValueError('Patente ya registrada')
        self._vehiculos[vehiculo.get_patente()] = vehiculo

    def xǁGestorFlotaǁregistrar__mutmut_1(self, vehiculo) -> None:
        if vehiculo.get_patente() not in self._vehiculos:
            raise ValueError('Patente ya registrada')
        self._vehiculos[vehiculo.get_patente()] = vehiculo

    def xǁGestorFlotaǁregistrar__mutmut_2(self, vehiculo) -> None:
        if vehiculo.get_patente() in self._vehiculos:
            raise ValueError(None)
        self._vehiculos[vehiculo.get_patente()] = vehiculo

    def xǁGestorFlotaǁregistrar__mutmut_3(self, vehiculo) -> None:
        if vehiculo.get_patente() in self._vehiculos:
            raise ValueError('XXPatente ya registradaXX')
        self._vehiculos[vehiculo.get_patente()] = vehiculo

    def xǁGestorFlotaǁregistrar__mutmut_4(self, vehiculo) -> None:
        if vehiculo.get_patente() in self._vehiculos:
            raise ValueError('patente ya registrada')
        self._vehiculos[vehiculo.get_patente()] = vehiculo

    def xǁGestorFlotaǁregistrar__mutmut_5(self, vehiculo) -> None:
        if vehiculo.get_patente() in self._vehiculos:
            raise ValueError('PATENTE YA REGISTRADA')
        self._vehiculos[vehiculo.get_patente()] = vehiculo

    def xǁGestorFlotaǁregistrar__mutmut_6(self, vehiculo) -> None:
        if vehiculo.get_patente() in self._vehiculos:
            raise ValueError('Patente ya registrada')
        self._vehiculos[vehiculo.get_patente()] = None

    @_mutmut_mutated(mutants_xǁGestorFlotaǁasignar__mutmut)
    def asignar(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('Vehículo no encontrado')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(legajo):
            raise ValueError('Legajo inválido según ValidadorLegajo')
        resultado = self._vehiculos[patente].asignar(legajo, km)
        self._asignaciones += 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_orig(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('Vehículo no encontrado')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(legajo):
            raise ValueError('Legajo inválido según ValidadorLegajo')
        resultado = self._vehiculos[patente].asignar(legajo, km)
        self._asignaciones += 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_1(self, patente: str, legajo: str, km: float) -> str:
        if patente in self._vehiculos:
            raise KeyError('Vehículo no encontrado')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(legajo):
            raise ValueError('Legajo inválido según ValidadorLegajo')
        resultado = self._vehiculos[patente].asignar(legajo, km)
        self._asignaciones += 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_2(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError(None)
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(legajo):
            raise ValueError('Legajo inválido según ValidadorLegajo')
        resultado = self._vehiculos[patente].asignar(legajo, km)
        self._asignaciones += 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_3(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('XXVehículo no encontradoXX')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(legajo):
            raise ValueError('Legajo inválido según ValidadorLegajo')
        resultado = self._vehiculos[patente].asignar(legajo, km)
        self._asignaciones += 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_4(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('vehículo no encontrado')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(legajo):
            raise ValueError('Legajo inválido según ValidadorLegajo')
        resultado = self._vehiculos[patente].asignar(legajo, km)
        self._asignaciones += 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_5(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('VEHÍCULO NO ENCONTRADO')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(legajo):
            raise ValueError('Legajo inválido según ValidadorLegajo')
        resultado = self._vehiculos[patente].asignar(legajo, km)
        self._asignaciones += 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_6(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('Vehículo no encontrado')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = None
        if not validador.validar(legajo):
            raise ValueError('Legajo inválido según ValidadorLegajo')
        resultado = self._vehiculos[patente].asignar(legajo, km)
        self._asignaciones += 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_7(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('Vehículo no encontrado')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if validador.validar(legajo):
            raise ValueError('Legajo inválido según ValidadorLegajo')
        resultado = self._vehiculos[patente].asignar(legajo, km)
        self._asignaciones += 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_8(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('Vehículo no encontrado')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(None):
            raise ValueError('Legajo inválido según ValidadorLegajo')
        resultado = self._vehiculos[patente].asignar(legajo, km)
        self._asignaciones += 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_9(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('Vehículo no encontrado')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(legajo):
            raise ValueError(None)
        resultado = self._vehiculos[patente].asignar(legajo, km)
        self._asignaciones += 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_10(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('Vehículo no encontrado')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(legajo):
            raise ValueError('XXLegajo inválido según ValidadorLegajoXX')
        resultado = self._vehiculos[patente].asignar(legajo, km)
        self._asignaciones += 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_11(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('Vehículo no encontrado')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(legajo):
            raise ValueError('legajo inválido según validadorlegajo')
        resultado = self._vehiculos[patente].asignar(legajo, km)
        self._asignaciones += 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_12(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('Vehículo no encontrado')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(legajo):
            raise ValueError('LEGAJO INVÁLIDO SEGÚN VALIDADORLEGAJO')
        resultado = self._vehiculos[patente].asignar(legajo, km)
        self._asignaciones += 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_13(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('Vehículo no encontrado')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(legajo):
            raise ValueError('Legajo inválido según ValidadorLegajo')
        resultado = None
        self._asignaciones += 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_14(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('Vehículo no encontrado')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(legajo):
            raise ValueError('Legajo inválido según ValidadorLegajo')
        resultado = self._vehiculos[patente].asignar(None, km)
        self._asignaciones += 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_15(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('Vehículo no encontrado')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(legajo):
            raise ValueError('Legajo inválido según ValidadorLegajo')
        resultado = self._vehiculos[patente].asignar(legajo, None)
        self._asignaciones += 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_16(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('Vehículo no encontrado')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(legajo):
            raise ValueError('Legajo inválido según ValidadorLegajo')
        resultado = self._vehiculos[patente].asignar(km)
        self._asignaciones += 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_17(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('Vehículo no encontrado')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(legajo):
            raise ValueError('Legajo inválido según ValidadorLegajo')
        resultado = self._vehiculos[patente].asignar(legajo, )
        self._asignaciones += 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_18(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('Vehículo no encontrado')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(legajo):
            raise ValueError('Legajo inválido según ValidadorLegajo')
        resultado = self._vehiculos[patente].asignar(legajo, km)
        self._asignaciones = 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_19(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('Vehículo no encontrado')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(legajo):
            raise ValueError('Legajo inválido según ValidadorLegajo')
        resultado = self._vehiculos[patente].asignar(legajo, km)
        self._asignaciones -= 1
        return resultado

    def xǁGestorFlotaǁasignar__mutmut_20(self, patente: str, legajo: str, km: float) -> str:
        if patente not in self._vehiculos:
            raise KeyError('Vehículo no encontrado')
        # Cambio C: delega validación de legajo a ValidadorLegajo
        validador = ValidadorLegajo()
        if not validador.validar(legajo):
            raise ValueError('Legajo inválido según ValidadorLegajo')
        resultado = self._vehiculos[patente].asignar(legajo, km)
        self._asignaciones += 2
        return resultado

    def get_total_asignaciones(self) -> int:
        return self._asignaciones

    @classmethod
    @_mutmut_mutated(mutants_xǁGestorFlotaǁ_reset_para_tests__mutmut, is_classmethod = True)
    def _reset_para_tests(cls):
        cls._instancia = None

    @classmethod
    def xǁGestorFlotaǁ_reset_para_tests__mutmut_orig(cls):
        cls._instancia = None

    @classmethod
    def xǁGestorFlotaǁ_reset_para_tests__mutmut_1(cls):
        cls._instancia = ""

mutants_xǁGestorFlotaǁ__init____mutmut['_mutmut_orig'] = GestorFlota.xǁGestorFlotaǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁ__init____mutmut['xǁGestorFlotaǁ__init____mutmut_1'] = GestorFlota.xǁGestorFlotaǁ__init____mutmut_1 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁ__init____mutmut['xǁGestorFlotaǁ__init____mutmut_2'] = GestorFlota.xǁGestorFlotaǁ__init____mutmut_2 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁ__init____mutmut['xǁGestorFlotaǁ__init____mutmut_3'] = GestorFlota.xǁGestorFlotaǁ__init____mutmut_3 # type: ignore # mutmut generated

mutants_xǁGestorFlotaǁget_instancia__mutmut['_mutmut_orig'] = GestorFlota.xǁGestorFlotaǁget_instancia__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁget_instancia__mutmut['xǁGestorFlotaǁget_instancia__mutmut_1'] = GestorFlota.xǁGestorFlotaǁget_instancia__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁget_instancia__mutmut['xǁGestorFlotaǁget_instancia__mutmut_2'] = GestorFlota.xǁGestorFlotaǁget_instancia__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁget_instancia__mutmut['xǁGestorFlotaǁget_instancia__mutmut_3'] = GestorFlota.xǁGestorFlotaǁget_instancia__mutmut_3 # type: ignore # mutmut generated

mutants_xǁGestorFlotaǁregistrar__mutmut['_mutmut_orig'] = GestorFlota.xǁGestorFlotaǁregistrar__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁregistrar__mutmut['xǁGestorFlotaǁregistrar__mutmut_1'] = GestorFlota.xǁGestorFlotaǁregistrar__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁregistrar__mutmut['xǁGestorFlotaǁregistrar__mutmut_2'] = GestorFlota.xǁGestorFlotaǁregistrar__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁregistrar__mutmut['xǁGestorFlotaǁregistrar__mutmut_3'] = GestorFlota.xǁGestorFlotaǁregistrar__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁregistrar__mutmut['xǁGestorFlotaǁregistrar__mutmut_4'] = GestorFlota.xǁGestorFlotaǁregistrar__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁregistrar__mutmut['xǁGestorFlotaǁregistrar__mutmut_5'] = GestorFlota.xǁGestorFlotaǁregistrar__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁregistrar__mutmut['xǁGestorFlotaǁregistrar__mutmut_6'] = GestorFlota.xǁGestorFlotaǁregistrar__mutmut_6 # type: ignore # mutmut generated

mutants_xǁGestorFlotaǁasignar__mutmut['_mutmut_orig'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_1'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_1 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_2'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_2 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_3'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_3 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_4'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_4 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_5'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_5 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_6'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_6 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_7'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_7 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_8'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_8 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_9'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_9 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_10'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_10 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_11'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_11 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_12'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_12 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_13'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_13 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_14'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_14 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_15'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_15 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_16'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_16 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_17'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_17 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_18'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_18 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_19'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_19 # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁasignar__mutmut['xǁGestorFlotaǁasignar__mutmut_20'] = GestorFlota.xǁGestorFlotaǁasignar__mutmut_20 # type: ignore # mutmut generated

mutants_xǁGestorFlotaǁ_reset_para_tests__mutmut['_mutmut_orig'] = GestorFlota.xǁGestorFlotaǁ_reset_para_tests__mutmut_orig # type: ignore # mutmut generated
mutants_xǁGestorFlotaǁ_reset_para_tests__mutmut['xǁGestorFlotaǁ_reset_para_tests__mutmut_1'] = GestorFlota.xǁGestorFlotaǁ_reset_para_tests__mutmut_1 # type: ignore # mutmut generated
