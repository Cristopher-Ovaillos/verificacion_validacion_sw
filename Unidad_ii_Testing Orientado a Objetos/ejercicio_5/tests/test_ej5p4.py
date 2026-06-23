import threading
import pytest
from flota.gestor_flota import GestorFlota


def test_singleton_ts():
    instancias_obtenidas = []
    barrera = threading.Barrier(50)

    def obtener_instancia():
        barrera.wait()
        instancia = GestorFlota.get_instancia()
        instancias_obtenidas.append(instancia)

    hilos = [threading.Thread(target=obtener_instancia) for _ in range(50)]
    for hilo in hilos:
        hilo.start()
    for hilo in hilos:
        hilo.join()

    primera_instancia = instancias_obtenidas[0]
    for i in range(1, len(instancias_obtenidas)):
        assert instancias_obtenidas[i] is primera_instancia, f"Instancia {i} no es la misma que la primera instancia"
