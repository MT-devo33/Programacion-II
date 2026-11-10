package CodEjer01;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

// Agregación: Carrera -> Docente
public class Carrera {
    private final String nombre;
    private final List<Docente> docentes = new ArrayList<>();

    public Carrera(String nombre) {
        this.nombre = nombre;
    }

    // La Carrera AGREGA a las partes ya existentes
    public void agregarDocente(Docente docente) {
        docentes.add(docente);
    }

    public String getNombre() {
        return nombre;
    }

    public List<Docente> getDocentes() {
        return Collections.unmodifiableList(docentes);
    }
}
