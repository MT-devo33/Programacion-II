public class Camara extends Sensor {
    public String resolucion;

    public Camara(String id, String resolucion) {
        super(id);
        this.tipo = "Cámara";
        this.resolucion = resolucion;
    }

    public String toString() {
        return super.toString() + ", Resolución: " + this.resolucion;
    }
}