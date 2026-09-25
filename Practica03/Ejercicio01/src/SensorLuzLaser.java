public class SensorLuzLaser extends Sensor implements ISensorLuzLaser {
    public int alcance;

    public SensorLuzLaser(String id, int alcance) {
        super(id);
        this.tipo = "Luz Laser";
        this.alcance = alcance;
    }

    public String toString() {
        return super.toString() + ", Alcance: " + this.alcance;
    }
}