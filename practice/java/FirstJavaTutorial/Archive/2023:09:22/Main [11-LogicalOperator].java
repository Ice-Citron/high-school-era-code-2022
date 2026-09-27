
import java.util.Scanner;
import java.util.Random;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);
        Random random = new Random();

        Boolean a;
        Boolean b;

        //System.out.println();
        //a = scanner.nextBoolean();
        //System.out.println();
        //b = scanner.nextBoolean();

        a = random.nextBoolean();
        b = random.nextBoolean();

        if((!a && b) || (!b)){
            System.out.println("You stink haha!");
        }





    }
}
