import pytest
from modelo import Auto, EstadoVehiculo


@pytest.fixture
def auto_consistente():
    return Auto(patente="ABC-123", km=100, puertas=4, estado=EstadoVehiculo.DISPONIBLE)


class TestParticionCategoria:

    def test_asignar_exito_P1_P4_P7(self, auto_consistente):
        legajo, kms = "A123", 200
        retorno = auto_consistente.asignar(legajo, kms)
        assert auto_consistente.get_estado() == EstadoVehiculo.EN_USO
        assert auto_consistente.get_conductor() == legajo
        assert str(kms) in retorno
        assert auto_consistente.verificar_invariante() is True

    def test_asignar_error_estado_no_disponible_P1_P4_P8(self):
        auto = Auto("ABC-123", 100, 4, EstadoVehiculo.MANTENIMIENTO)
        estado_original = auto.get_estado()
        with pytest.raises(PermissionError):
            auto.asignar("A123", 100)
        assert auto.get_estado() == estado_original
        assert auto.verificar_invariante() is True

    def test_asignar_error_legajo_vacio_P2_P4_P7(self, auto_consistente):
        estado_original = auto_consistente.get_estado()
        with pytest.raises(ValueError):
            auto_consistente.asignar("", 100)
        assert auto_consistente.get_estado() == estado_original
        assert auto_consistente.get_conductor() is None
        assert auto_consistente.verificar_invariante() is True

    def test_asignar_error_legajo_corto_P3_P4_P7(self, auto_consistente):
        estado_original = auto_consistente.get_estado()
        with pytest.raises(ValueError):
            auto_consistente.asignar("ABC", 100)
        assert auto_consistente.get_estado() == estado_original
        assert auto_consistente.get_conductor() is None
        assert auto_consistente.verificar_invariante() is True

    def test_asignar_error_km_no_positivo_P1_P5_P7(self, auto_consistente):
        estado_original = auto_consistente.get_estado()
        with pytest.raises(ValueError):
            auto_consistente.asignar("A123", 0)
        assert auto_consistente.get_estado() == estado_original
        assert auto_consistente.get_conductor() is None
        assert auto_consistente.verificar_invariante() is True

    def test_asignar_error_km_excede_maximo_P1_P6_P7(self, auto_consistente):
        estado_original = auto_consistente.get_estado()
        with pytest.raises(ValueError):
            auto_consistente.asignar("A123", 501)
        assert auto_consistente.get_estado() == estado_original
        assert auto_consistente.get_conductor() is None
        assert auto_consistente.verificar_invariante() is True
