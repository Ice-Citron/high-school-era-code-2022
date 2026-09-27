import java.util.InputMismatchException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        Scanner scanner = new Scanner(System.in);

        try {
            System.out.println("Enter a number to divide: ");
            int x = scanner.nextInt();
            scanner.nextLine();

            System.out.println("Enter a number to be divided by: ");
            int y = scanner.nextInt();
            scanner.nextLine();

            //double z = (double) x / y;
            int z = x / y;
            System.out.println("The number is: " + z);

        }
        catch (ArithmeticException e) {
            System.out.println("You can't divided by zero lol.");
        }
        catch (InputMismatchException e) {
            System.out.println("Please enter a number instead lol!");
            //System.out.println(e);
        }
        catch (Exception e) {
            System.out.println("Something went wrong! - " + e);
        }
        finally {
            scanner.close();
        }

    }
}
