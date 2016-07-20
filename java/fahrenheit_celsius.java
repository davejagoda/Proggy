/* columns don't matter in Java
 to compile:
 javac fahrenheit_celsius.java */

public class fahrenheit_celsius {
    public static void main(String[] args) {
        double fahr, celsius;
        int lower, upper, step;

        lower =   0; /* lower limit of temperature table */
        upper = 300; /* upper limit of temperature table */
        step  =  20; /* step size */

        fahr = lower;
        while (fahr <= upper) {
            celsius = (5.0/9.0) * (fahr-32.0);
            System.out.printf("%3.0f %6.1f\n", fahr, celsius);
            fahr = fahr + step;
        }
    }
}
