package CodEjer01;

import java.time.LocalDate;

//Inscripcion implementa Calificable
public class Inscripcion implements Calificable {
 private final Estudiante estudiante;
 private final Materia materia;
 private final LocalDate fecha;
 private double nota;

 public Inscripcion(Estudiante estudiante, Materia materia, LocalDate fecha) {
     this.estudiante = estudiante;
     this.materia = materia;
     this.fecha = fecha;
 }

 public void registrarNota(double nota) {
     if (nota < 0 || nota > 100) {
         throw new IllegalArgumentException("La nota debe estar entre 0 y 100");
     }
     this.nota = nota;
 }

 @Override
 public double calcularNota() {
     return nota;
 }

 public Estudiante getEstudiante() {
     return estudiante;
 }

 public Materia getMateria() {
     return materia;
 }

 public LocalDate getFecha() {
     return fecha;
 }
}
