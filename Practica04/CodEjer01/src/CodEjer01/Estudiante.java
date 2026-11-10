package CodEjer01;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Estudiante extends Persona {
    private final String codigo;
    // Asociación: el estudiante conoce sus inscripciones
    private final List<Inscripcion> inscripciones = new ArrayList<>();

    public Estudiante(String nombre, String ci, String codigo) {
        super(nombre, ci);
        this.codigo = codigo;
    }

    public String getCodigo() {
        return codigo;
    }

    public Inscripcion inscribirse(Materia materia) {
        Inscripcion inscripcion = new Inscripcion(this, materia, LocalDate.now());
        inscripciones.add(inscripcion);
        materia.registrarInscripcion(inscripcion);
        return inscripcion;
    }

    public List<Inscripcion> getInscripciones() {
        return Collections.unmodifiableList(inscripciones);
    }

    @Override
    public String toString() {
        return "Estudiante " + getNombre() + " (código " + codigo + ")";
    }
}
