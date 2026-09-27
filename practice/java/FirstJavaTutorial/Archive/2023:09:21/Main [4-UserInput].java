
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        System.out.println("What is your name?");
        String name = scanner.nextLine();

        System.out.println("How old are you?");
        int age = scanner.nextInt();
        scanner.nextLine(); //need to call nextLine after nextInt, because nextInt haven't skipped to \n

        System.out.println("What is your favourite food?");
        String food = scanner.nextLine();

        System.out.println("Hello " + name);
        System.out.println("You are " + age + " years old.");
        System.out.println("And your favourite food is " + food + "!");


    }
}
