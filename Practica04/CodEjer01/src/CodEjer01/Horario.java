package CodEjer01;

import java.time.LocalDate;

public class Horario {
    private final LocalDate fecha;
    private final String aula;

    public Horario(LocalDate fecha, String aula) {
        this.fecha = fecha;
        this.aula = aula;
    }

    public LocalDate getFecha() {
        return fecha;
    }

    public String getAula() {
        return aula;
    }
}
