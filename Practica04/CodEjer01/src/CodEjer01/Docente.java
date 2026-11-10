package CodEjer01;

import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

public class Docente extends Persona {
    private final String especialidad;
    // Asociación: el docente conoce las materias que dicta
    private final List<Materia> materias = new ArrayList<>();

    public Docente(String nombre, String ci, String especialidad) {
        super(nombre, ci);
        this.especialidad = especialidad;
    }

    public void dictar(Materia materia) {
        materias.add(materia);
        materia.setDocente(this);
    }

    // Dependencia: Acta se crea y se devuelve, pero NO se guarda como atributo
    public Acta generarActa(Materia materia) {
        return new Acta(materia);
    }

    public List<Materia> getMaterias() {
        return Collections.unmodifiableList(materias);
    }

    @Override
    public String toString() {
        return "Docente " + getNombre() + " (" + especialidad + ")";
    }
}
