Feature: Gestión de asignaciones de la flota vehicular
  Como jefe de flota
  Quiero asignar y liberar vehículos
  Para controlar el uso de la flota


  Background:
    Given la flota tiene registrado el vehículo con patente 'ABC123'
    And   el vehículo es un Auto con 0 km actuales


  Scenario: Asignación exitosa a conductor habilitado
    Given el vehículo está disponible
    When  el conductor con legajo 'L-001' solicita el vehículo por 450 km
    Then  el vehículo debe estar en estado EN_USO
    And   el conductor 'L-001' debe figurar como responsable


  Scenario: Liberación y actualización de kilómetros
    Given el vehículo está asignado al conductor 'L-001' por 450 km
    When  el conductor libera el vehículo habiendo recorrido 380 km
    Then  el vehículo debe estar en estado DISPONIBLE
    And   el odómetro del vehículo debe registrar 380 km


  Scenario: Intento de asignación de vehículo en mantenimiento
    Given el vehículo está en mantenimiento
    When  el conductor con legajo 'L-002' intenta asignarlo por 100 km
    Then  el sistema debe rechazar la operación
    And   el vehículo debe seguir en estado MANTENIMIENTO


  Scenario Outline: Validación de kilómetros estimados
    Given el vehículo está disponible
    When  el conductor solicita el vehículo por <km> km
    Then  el resultado debe ser <resultado>


    Examples:
      | km  | resultado |
      |   1 | exitoso   |
      | 800 | exitoso   |
      |   0 | error     |
      | 801 | error     |


  Scenario: Flujo completo de mantenimiento — detecta bug en ServicioMantenimiento.liberar()
    Given el vehículo está disponible
    And   el vehículo está asignado al conductor 'L-001' por 300 km
    When  el conductor libera el vehículo habiendo recorrido 280 km
    Then  el vehículo debe estar en estado DISPONIBLE
    When  se envía el vehículo a mantenimiento
    Then  el vehículo debe estar en estado MANTENIMIENTO
    Given el vehículo ingresa al taller
    When  el vehículo sale del taller
    Then  el vehículo debe estar en estado DISPONIBLE
