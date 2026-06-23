package flota;

public class TestMotoHeredadi extends VehiculoTest{
    @Override
    protected Vehiculo crearVehiculo(double km) {
        // Sustitución: Se inyecta una Moto
        return new Moto("MOT-222", km);
    }
}
