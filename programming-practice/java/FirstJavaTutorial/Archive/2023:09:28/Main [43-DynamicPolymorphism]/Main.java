import java.util.Scanner;

public class Main {
    public static void main(String[] args) {

        //polymorphism = for objects to be able to be identified as many different forms
        //dynamic      = post-compilation (during runtime)

        Scanner scanner = new Scanner(System.in);
        Animal animal;

        System.out.println("What animal do you want?");
        System.out.println("(1=dog) or (2=cat)");
        int choice = scanner.nextInt();

        if (choice == 1) {
            animal = new Dog();
            animal.Speak();
        }
        else if (choice == 2) {
            animal = new Cat();
            animal.Speak();
        }
        else {
            animal = new Animal();
            System.out.println("That choice was invalid.");
            animal.Speak();
        }

    }
}
