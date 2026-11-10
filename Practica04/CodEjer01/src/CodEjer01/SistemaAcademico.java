package CodEjer01;

import java.time.LocalDate;
import java.util.Arrays;
import java.util.List;

public class SistemaAcademico {
    public static void main(String[] args) {
        // Composición: la Universidad crea sus Carreras
        Universidad umsa = new Universidad("UMSA");
        Carrera informatica = umsa.crearCarrera("Informática");
        
        // Agregación: los Docentes existen antes e independientemente de la Materia
        Docente docente = new Docente("Ana Alba", "1234567", "Ingeniería de Software");
        informatica.agregarDocente(docente);
        
        // Asociación: el Docente dicta una Materia
        Materia poo = new Materia("INF-121", 6);
        docente.dictar(poo);
        
        // Composición: la Materia crea sus Horarios
        poo.agregarHorario(LocalDate.of(2026, 7, 2), "Aula 101");
        poo.agregarHorario(LocalDate.of(2026, 7, 9), "Aula 101");
        
        // Asociación entre Estudiante e Inscripcion
        Estudiante e1 = new Estudiante("Carlos Flores", "7654321", "E-001");
        Estudiante e2 = new Estudiante("Maria Salas", "7654322", "E-002");
        Inscripcion i1 = e1.inscribirse(poo);
        Inscripcion i2 = e2.inscribirse(poo);
        
        // Registro de notas solicitado en el ejercicio 1
        i1.registrarNota(85);
        i2.registrarNota(92);
        
        // Herencia y polimorfismo
        List<Persona> personas = Arrays.asList(docente, e1, e2);
        personas.forEach(p -> System.out.println(p));
        
        // La inscripcion se usa a través de la interfaz Calificable
        Calificable c = i1;
        System.out.println("Nota de " + e1.getNombre() + ": " + c.calcularNota());
        
        // Dependencia: el Docente usa Acta solo dentro de un método
        System.out.println("\n--- GENERANDO ACTA ---");
        Acta acta = docente.generarActa(poo);
        System.out.println(acta);
    }
}
