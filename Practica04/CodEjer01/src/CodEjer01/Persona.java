package CodEjer01;

//Herencia: Persona (abstracta) <- Estudiante, Docente
public abstract class Persona {
 private final String nombre;
 private final String ci;

 protected Persona(String nombre, String ci) {
     this.nombre = nombre;
     this.ci = ci;
 }

 public String getNombre() {
     return nombre;
 }

 public String getCi() {
     return ci;
 }

 public abstract String toString();
}
