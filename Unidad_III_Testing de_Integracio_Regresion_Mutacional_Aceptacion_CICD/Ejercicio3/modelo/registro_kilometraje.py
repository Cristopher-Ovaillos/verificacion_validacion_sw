# Proveniencia: Copiado de Unidad_III/Ejercicio1/flota/registro_kilometraje.py
# Original:      Nuevo en Unidad III
class RegistroKilometraje:
    def __init__(self):
        self._historial = {}

    def registrar(self, patente: str, km: float) -> None:
        self._historial[patente] = self._historial.get(patente, 0) + km

    def obtener_km(self, patente: str) -> float:
        return self._historial.get(patente, 0)
