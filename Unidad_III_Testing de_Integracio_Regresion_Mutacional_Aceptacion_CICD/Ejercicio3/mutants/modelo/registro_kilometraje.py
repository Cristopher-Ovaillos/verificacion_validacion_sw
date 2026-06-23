# Proveniencia: Copiado de Unidad_III/Ejercicio1/flota/registro_kilometraje.py
# Original:      Nuevo en Unidad III


from mutmut.mutation.trampoline import wrap_in_trampoline as _mutmut_mutated, MutantDict
mutants_xǁRegistroKilometrajeǁ__init____mutmut: MutantDict = {}  # type: ignore
mutants_xǁRegistroKilometrajeǁregistrar__mutmut: MutantDict = {}  # type: ignore
mutants_xǁRegistroKilometrajeǁobtener_km__mutmut: MutantDict = {}  # type: ignore
class RegistroKilometraje:
    @_mutmut_mutated(mutants_xǁRegistroKilometrajeǁ__init____mutmut)
    def __init__(self):
        self._historial = {}
    def xǁRegistroKilometrajeǁ__init____mutmut_orig(self):
        self._historial = {}
    def xǁRegistroKilometrajeǁ__init____mutmut_1(self):
        self._historial = None

    @_mutmut_mutated(mutants_xǁRegistroKilometrajeǁregistrar__mutmut)
    def registrar(self, patente: str, km: float) -> None:
        self._historial[patente] = self._historial.get(patente, 0) + km

    def xǁRegistroKilometrajeǁregistrar__mutmut_orig(self, patente: str, km: float) -> None:
        self._historial[patente] = self._historial.get(patente, 0) + km

    def xǁRegistroKilometrajeǁregistrar__mutmut_1(self, patente: str, km: float) -> None:
        self._historial[patente] = None

    def xǁRegistroKilometrajeǁregistrar__mutmut_2(self, patente: str, km: float) -> None:
        self._historial[patente] = self._historial.get(patente, 0) - km

    def xǁRegistroKilometrajeǁregistrar__mutmut_3(self, patente: str, km: float) -> None:
        self._historial[patente] = self._historial.get(None, 0) + km

    def xǁRegistroKilometrajeǁregistrar__mutmut_4(self, patente: str, km: float) -> None:
        self._historial[patente] = self._historial.get(patente, None) + km

    def xǁRegistroKilometrajeǁregistrar__mutmut_5(self, patente: str, km: float) -> None:
        self._historial[patente] = self._historial.get(0) + km

    def xǁRegistroKilometrajeǁregistrar__mutmut_6(self, patente: str, km: float) -> None:
        self._historial[patente] = self._historial.get(patente, ) + km

    def xǁRegistroKilometrajeǁregistrar__mutmut_7(self, patente: str, km: float) -> None:
        self._historial[patente] = self._historial.get(patente, 1) + km

    @_mutmut_mutated(mutants_xǁRegistroKilometrajeǁobtener_km__mutmut)
    def obtener_km(self, patente: str) -> float:
        return self._historial.get(patente, 0)

    def xǁRegistroKilometrajeǁobtener_km__mutmut_orig(self, patente: str) -> float:
        return self._historial.get(patente, 0)

    def xǁRegistroKilometrajeǁobtener_km__mutmut_1(self, patente: str) -> float:
        return self._historial.get(None, 0)

    def xǁRegistroKilometrajeǁobtener_km__mutmut_2(self, patente: str) -> float:
        return self._historial.get(patente, None)

    def xǁRegistroKilometrajeǁobtener_km__mutmut_3(self, patente: str) -> float:
        return self._historial.get(0)

    def xǁRegistroKilometrajeǁobtener_km__mutmut_4(self, patente: str) -> float:
        return self._historial.get(patente, )

    def xǁRegistroKilometrajeǁobtener_km__mutmut_5(self, patente: str) -> float:
        return self._historial.get(patente, 1)

mutants_xǁRegistroKilometrajeǁ__init____mutmut['_mutmut_orig'] = RegistroKilometraje.xǁRegistroKilometrajeǁ__init____mutmut_orig # type: ignore # mutmut generated
mutants_xǁRegistroKilometrajeǁ__init____mutmut['xǁRegistroKilometrajeǁ__init____mutmut_1'] = RegistroKilometraje.xǁRegistroKilometrajeǁ__init____mutmut_1 # type: ignore # mutmut generated

mutants_xǁRegistroKilometrajeǁregistrar__mutmut['_mutmut_orig'] = RegistroKilometraje.xǁRegistroKilometrajeǁregistrar__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRegistroKilometrajeǁregistrar__mutmut['xǁRegistroKilometrajeǁregistrar__mutmut_1'] = RegistroKilometraje.xǁRegistroKilometrajeǁregistrar__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRegistroKilometrajeǁregistrar__mutmut['xǁRegistroKilometrajeǁregistrar__mutmut_2'] = RegistroKilometraje.xǁRegistroKilometrajeǁregistrar__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRegistroKilometrajeǁregistrar__mutmut['xǁRegistroKilometrajeǁregistrar__mutmut_3'] = RegistroKilometraje.xǁRegistroKilometrajeǁregistrar__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRegistroKilometrajeǁregistrar__mutmut['xǁRegistroKilometrajeǁregistrar__mutmut_4'] = RegistroKilometraje.xǁRegistroKilometrajeǁregistrar__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRegistroKilometrajeǁregistrar__mutmut['xǁRegistroKilometrajeǁregistrar__mutmut_5'] = RegistroKilometraje.xǁRegistroKilometrajeǁregistrar__mutmut_5 # type: ignore # mutmut generated
mutants_xǁRegistroKilometrajeǁregistrar__mutmut['xǁRegistroKilometrajeǁregistrar__mutmut_6'] = RegistroKilometraje.xǁRegistroKilometrajeǁregistrar__mutmut_6 # type: ignore # mutmut generated
mutants_xǁRegistroKilometrajeǁregistrar__mutmut['xǁRegistroKilometrajeǁregistrar__mutmut_7'] = RegistroKilometraje.xǁRegistroKilometrajeǁregistrar__mutmut_7 # type: ignore # mutmut generated

mutants_xǁRegistroKilometrajeǁobtener_km__mutmut['_mutmut_orig'] = RegistroKilometraje.xǁRegistroKilometrajeǁobtener_km__mutmut_orig # type: ignore # mutmut generated
mutants_xǁRegistroKilometrajeǁobtener_km__mutmut['xǁRegistroKilometrajeǁobtener_km__mutmut_1'] = RegistroKilometraje.xǁRegistroKilometrajeǁobtener_km__mutmut_1 # type: ignore # mutmut generated
mutants_xǁRegistroKilometrajeǁobtener_km__mutmut['xǁRegistroKilometrajeǁobtener_km__mutmut_2'] = RegistroKilometraje.xǁRegistroKilometrajeǁobtener_km__mutmut_2 # type: ignore # mutmut generated
mutants_xǁRegistroKilometrajeǁobtener_km__mutmut['xǁRegistroKilometrajeǁobtener_km__mutmut_3'] = RegistroKilometraje.xǁRegistroKilometrajeǁobtener_km__mutmut_3 # type: ignore # mutmut generated
mutants_xǁRegistroKilometrajeǁobtener_km__mutmut['xǁRegistroKilometrajeǁobtener_km__mutmut_4'] = RegistroKilometraje.xǁRegistroKilometrajeǁobtener_km__mutmut_4 # type: ignore # mutmut generated
mutants_xǁRegistroKilometrajeǁobtener_km__mutmut['xǁRegistroKilometrajeǁobtener_km__mutmut_5'] = RegistroKilometraje.xǁRegistroKilometrajeǁobtener_km__mutmut_5 # type: ignore # mutmut generated
