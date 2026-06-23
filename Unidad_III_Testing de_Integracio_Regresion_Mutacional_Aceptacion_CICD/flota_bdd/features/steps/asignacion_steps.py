from behave import given, when, then
from src.auto import Auto, EstadoVehiculo
from src.gestor_flota import GestorFlota
from src.registro_kilometraje import RegistroKilometraje
from src.servicio_mantenimiento import ServicioMantenimiento


@given('la flota tiene registrado el vehículo con patente \'{patente}\'')
def step_registrar_vehiculo(context, patente):
    context.gestor = GestorFlota.get_instancia()
    context.vehiculo = Auto(patente, 'Toyota', 2020, 0.0, 4)
    context.patente = patente
    context.gestor.registrar(context.vehiculo)


@given('el vehículo es un Auto con {km:d} km actuales')
def step_km_actuales(context, km):
    assert context.vehiculo.get_km() == km


@given('el vehículo está disponible')
def step_vehiculo_disponible(context):
    assert context.vehiculo.get_estado() == EstadoVehiculo.DISPONIBLE


@given('el vehículo está asignado al conductor \'{legajo}\' por {km:d} km')
def step_vehiculo_asignado(context, legajo, km):
    context.vehiculo.asignar(legajo, km)


@given('el vehículo está en mantenimiento')
def step_vehiculo_mantenimiento(context):
    context.vehiculo.enviar_mantenimiento()


@when('el conductor con legajo \'{legajo}\' solicita el vehículo por {km:d} km')
def step_solicitar_conductor(context, legajo, km):
    try:
        context.resultado = context.gestor.asignar(context.patente, legajo, km)
        context.error = None
    except (ValueError, PermissionError, KeyError) as e:
        context.error = str(e)
        context.resultado = None


@when('el conductor libera el vehículo habiendo recorrido {km:d} km')
def step_liberar(context, km):
    context.vehiculo.liberar(km)


@when('el conductor con legajo \'{legajo}\' intenta asignarlo por {km:d} km')
def step_intentar_asignar(context, legajo, km):
    try:
        context.resultado = context.gestor.asignar(context.patente, legajo, km)
        context.error = None
    except (ValueError, PermissionError, KeyError) as e:
        context.error = str(e)
        context.resultado = None


@when('el conductor solicita el vehículo por {km:d} km')
def step_solicitar_sin_legajo(context, km):
    try:
        context.resultado = context.gestor.asignar(context.patente, 'L-000', km)
        context.error = None
    except (ValueError, PermissionError, KeyError) as e:
        context.error = str(e)
        context.resultado = None


@then('el vehículo debe estar en estado {estado}')
def step_verificar_estado(context, estado):
    assert context.vehiculo.get_estado().name == estado, \
        f'Esperado {estado}, obtenido {context.vehiculo.get_estado().name}'


@then('el conductor \'{legajo}\' debe figurar como responsable')
def step_verificar_conductor(context, legajo):
    assert context.vehiculo.get_conductor() == legajo, \
        f'Esperado {legajo}, obtenido {context.vehiculo.get_conductor()}'


@then('el odómetro del vehículo debe registrar {km:d} km')
def step_verificar_odometro(context, km):
    assert context.vehiculo.get_km() == km, \
        f'Esperado {km}, obtenido {context.vehiculo.get_km()}'


@then('el sistema debe rechazar la operación')
def step_verificar_rechazo(context):
    assert context.error is not None, \
        'Se esperaba un error pero la operación fue exitosa'


@then('el vehículo debe seguir en estado {estado}')
def step_verificar_sigue_estado(context, estado):
    assert context.vehiculo.get_estado().name == estado, \
        f'Esperado {estado}, obtenido {context.vehiculo.get_estado().name}'


@then('el resultado debe ser {resultado}')
def step_verificar_resultado(context, resultado):
    if resultado == 'exitoso':
        assert context.error is None and context.resultado is not None, \
            f'Se esperaba éxito pero se obtuvo error: {context.error}'
    else:
        assert context.error is not None, \
            f'Se esperaba error pero la operación fue exitosa: {context.resultado}'


@when('se envía el vehículo a mantenimiento')
def step_enviar_mantenimiento(context):
    context.vehiculo.enviar_mantenimiento()


@given('el vehículo ingresa al taller')
def step_ingresar_taller(context):
    context.registro = RegistroKilometraje()
    context.servicio = ServicioMantenimiento(context.registro)
    context.servicio.ingresar(context.vehiculo)


@when('el vehículo sale del taller')
def step_salir_taller(context):
    context.servicio.liberar(context.vehiculo)
