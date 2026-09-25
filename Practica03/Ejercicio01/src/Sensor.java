public class Sensor {
    public String tipo = "Genérico";
    public String id;
    public boolean encendido;

    public Sensor(String id) {
        this.id = id;
        this.encendido = false;
    }

    public void activar() {
        this.encendido = true;
    }

    public void desactivar() {
        this.encendido = false;
    }

    public String toString() {
        return "Tipo: " + this.tipo + ", ID: " + this.id + ", Encendido: " + this.encendido;
    }
}