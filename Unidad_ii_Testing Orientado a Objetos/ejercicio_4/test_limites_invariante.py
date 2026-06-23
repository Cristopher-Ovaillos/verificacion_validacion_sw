import pytest
from modelo import Auto, EstadoVehiculo


@pytest.fixture
def auto_consistente():
    return Auto(patente="ABC-123", km=100, puertas=4, estado=EstadoVehiculo.DISPONIBLE)


class TestLimitesInvariante:

    def test_invariante_patente_limite_inconsistente_L_menos_epsilon(self):
        auto = Auto(patente="ABC12", km=0, puertas=2, estado=EstadoVehiculo.DISPONIBLE)
        assert auto.verificar_invariante() is False

    def test_invariante_patente_limite_L(self, auto_consistente):
        auto = Auto(patente="ABC123", km=100, puertas=4, estado=EstadoVehiculo.DISPONIBLE)
        assert auto.verificar_invariante() is True
        retorno = auto.asignar("A123", 200)
        assert auto.get_estado() == EstadoVehiculo.EN_USO
        assert auto.get_conductor() == "A123"
        assert auto.verificar_invariante() is True

    def test_invariante_patente_limite_L_mas_epsilon(self, auto_consistente):
        assert len(auto_consistente.get_patente()) == 7
        assert auto_consistente.verificar_invariante() is True
        retorno = auto_consistente.asignar("A123", 200)
        assert auto_consistente.get_estado() == EstadoVehiculo.EN_USO
        assert auto_consistente.verificar_invariante() is True

    def test_invariante_km_limite_inconsistente_L_menos_epsilon(self):
        auto = Auto(patente="ABC-123", km=-1, puertas=4, estado=EstadoVehiculo.DISPONIBLE)
        assert auto.verificar_invariante() is False

    def test_invariante_km_limite_L(self):
        auto = Auto(patente="ABC-123", km=0, puertas=4, estado=EstadoVehiculo.DISPONIBLE)
        assert auto.verificar_invariante() is True
        retorno = auto.asignar("A123", 100)
        assert auto.get_estado() == EstadoVehiculo.EN_USO
        assert auto.verificar_invariante() is True

    def test_invariante_km_limite_L_mas_epsilon(self):
        auto = Auto(patente="ABC-123", km=1, puertas=4, estado=EstadoVehiculo.DISPONIBLE)
        assert auto.verificar_invariante() is True
        retorno = auto.asignar("A123", 100)
        assert auto.get_estado() == EstadoVehiculo.EN_USO
        assert auto.verificar_invariante() is True

    def test_invariante_consistencia_estado_conductor_punto_consistente(self, auto_consistente):
        assert auto_consistente.get_conductor() is None
        assert auto_consistente.get_estado() == EstadoVehiculo.DISPONIBLE
        assert auto_consistente.verificar_invariante() is True
        retorno = auto_consistente.asignar("A123", 100)
        assert auto_consistente.get_conductor() == "A123"
        assert auto_consistente.get_estado() == EstadoVehiculo.EN_USO
        assert auto_consistente.verificar_invariante() is True

    def test_invariante_consistencia_estado_conductor_punto_inconsistente(self):
        auto = Auto(patente="ABC-123", km=100, puertas=4, estado=EstadoVehiculo.DISPONIBLE)
        auto._conductor = "A123"
        assert auto.verificar_invariante() is False

    @pytest.mark.parametrize("kms, esperado", [
        (0, ValueError),
        (1, "exito"),
        (500, "exito"),
        (501, ValueError)
    ])
    def test_limites_km_estimados_parametro(self, auto_consistente, kms, esperado):
        if esperado == ValueError:
            with pytest.raises(ValueError):
                auto_consistente.asignar("A123", kms)
            assert auto_consistente.get_estado() == EstadoVehiculo.DISPONIBLE
            assert auto_consistente.get_conductor() is None
        else:
            retorno = auto_consistente.asignar("A123", kms)
            assert auto_consistente.get_estado() == EstadoVehiculo.EN_USO
            assert auto_consistente.get_conductor() == "A123"
        assert auto_consistente.verificar_invariante() is True

    @pytest.mark.parametrize("legajo, esperado", [
        ("ABC", ValueError),
        ("A123", "exito"),
        ("A1234", "exito"),
    ])
    def test_limites_legajo_conductor_parametro(self, auto_consistente, legajo, esperado):
        if esperado == ValueError:
            with pytest.raises(ValueError):
                auto_consistente.asignar(legajo, 100)
            assert auto_consistente.get_estado() == EstadoVehiculo.DISPONIBLE
            assert auto_consistente.get_conductor() is None
        else:
            retorno = auto_consistente.asignar(legajo, 100)
            assert auto_consistente.get_estado() == EstadoVehiculo.EN_USO
            assert auto_consistente.get_conductor() == legajo
        assert auto_consistente.verificar_invariante() is True
