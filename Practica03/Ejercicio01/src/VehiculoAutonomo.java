public class VehiculoAutonomo extends Camara {
    private SensorLuzLaser sensorLaser;

    public VehiculoAutonomo(String id, String resolucion, int alcance) {
        super(id, resolucion);
        this.tipo = "Vehículo Autónomo";
        this.sensorLaser = new SensorLuzLaser(id, alcance);
    }

    public void activar() {
        super.activar();
        this.sensorLaser.activar();
    }

    public void desactivar() {
        super.desactivar();
        this.sensorLaser.desactivar();
    }

    public String toString() {
        return super.toString() + ", Alcance: " + this.sensorLaser.alcance;
    }
}