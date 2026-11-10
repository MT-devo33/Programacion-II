package CodEjer01;

import java.time.LocalDate;

//Dependencia: Docente usa Acta de forma temporal
public class Acta {
 private final LocalDate fecha = LocalDate.now();
 private final String contenido;

 public Acta(Materia materia) {
     StringBuilder sb = new StringBuilder();
     sb.append("ACTA ").append(materia.getCodigo()).append(" ").append(fecha).append('\n');
     for (Inscripcion i : materia.getInscripciones()) {
         sb.append(" ").append(i.getEstudiante().getNombre()).append(": ").append(i.calcularNota()).append('\n');
     }
     this.contenido = sb.toString();
 }

 @Override
 public String toString() {
     return contenido;
 }
}
