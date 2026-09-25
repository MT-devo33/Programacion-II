public class Main {
    public static void main(String[] args) {
        VehiculoAutonomo va = new VehiculoAutonomo("VH-001", "4K", 150);
        System.out.println(va.toString());
        va.activar();
        System.out.println(va.toString());
    }
}