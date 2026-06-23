import pytest
from flota.gestor_flota import GestorFlota


@pytest.fixture(scope="function")
def gestor_reset():
    gestor = GestorFlota.get_instancia()
    yield gestor
    GestorFlota._reset_para_tests()
