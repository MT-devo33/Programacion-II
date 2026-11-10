package CodEjer01;

import java.time.LocalDate;
import java.util.ArrayList;
import java.util.Collections;
import java.util.List;

// Composición: Materia -> Horario
public class Materia {
    private final String codigo;
    private final int creditos;
    private Docente docente;
    private final List<Horario> horarios = new ArrayList<>();
    private final List<Inscripcion> inscripciones = new ArrayList<>();

    public Materia(String codigo, int creditos) {
        this.codigo = codigo;
        this.creditos = creditos;
    }

    public Horario agregarHorario(LocalDate fecha, String aula) {
        Horario s = new Horario(fecha, aula);
        horarios.add(s);
        return s;
    }

    public void registrarInscripcion(Inscripcion inscripcion) {
        inscripciones.add(inscripcion);
    }

    public void setDocente(Docente docente) {
        this.docente = docente;
    }

    public String getCodigo() {
        return codigo;
    }

    public int getCreditos() {
        return creditos;
    }

    public Docente getDocente() {
        return docente;
    }

    public List<Horario> getHorarios() {
        return Collections.unmodifiableList(horarios);
    }

    public List<Inscripcion> getInscripciones() {
        return Collections.unmodifiableList(inscripciones);
    }
}
