import pytest
from modelo import Auto, EstadoVehiculo


class TestCoberturaCompleta:

    def test_getters_no_usados(self):
        auto = Auto("ABC-123", 100, 4, EstadoVehiculo.DISPONIBLE)
        assert auto.get_km() == 100
        assert auto.get_puertas() == 4

    def test_invariante_puertas_invalidas(self):
        auto = Auto("ABC-123", 100, 3, EstadoVehiculo.DISPONIBLE)
        assert auto.verificar_invariante() is False

    def test_invariante_puertas_validas_borde_2(self):
        auto = Auto("ABC-123", 100, 2, EstadoVehiculo.DISPONIBLE)
        assert auto.verificar_invariante() is True

    def test_invariante_puertas_validas_borde_5(self):
        auto = Auto("ABC-123", 100, 5, EstadoVehiculo.DISPONIBLE)
        assert auto.verificar_invariante() is True
