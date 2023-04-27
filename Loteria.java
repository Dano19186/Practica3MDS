import java.util.Random;

public class Loteria {
    public static void main(String[] args) {
        //Incluimos el número que nos ha devuelto en nuestro intento fallido
        int anterior = 814413627;
        boolean encontrado = false;
        int token;
        Random random;
        //Calculamos la hora de mi sistema en milisegundos
        long horaDelSistema = System.currentTimeMillis();
        //Ponemos un tiempo arbitrario de 1 min (en ms) como máximo desfase con el servidor
        for (int i = 0; i < 60000; i++) {
            //Buscamos la semilla de nuestra sesión que será cuando se genere el mismo resultado
            random = new Random(horaDelSistema - i);
            token = random.nextInt(1_234_000_100);
            if (anterior == token) {
                encontrado = true;
            }
            //Si encontramos la semilla, generamos el siguente número que será el correspondiente al siugiente que cree el servidor
            if (encontrado) {
                System.out.println(random.nextInt(1_234_000_100));
                System.exit(0);
            }

        }
    }
}
