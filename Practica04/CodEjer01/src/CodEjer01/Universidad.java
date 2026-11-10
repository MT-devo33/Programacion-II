package CodEjer01;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

// Composición: Universidad -> Carrera
public class Universidad {
    private final String nombre;
    private final List<Carrera> carreras = new ArrayList<>();

    public Universidad(String nombre) {
        this.nombre = nombre;
    }

    // La Universidad CREA a las partes (carreras: no existen fuera de la Universidad)
    public Carrera crearCarrera(String nombreCarrera) {
        Carrera d = new Carrera(nombreCarrera);
        carreras.add(d);
        return d;
    }

    public String getNombre() {
        return nombre;
    }

    public List<Carrera> getCarreras() {
        return Collections.unmodifiableList(carreras);
    }
}
