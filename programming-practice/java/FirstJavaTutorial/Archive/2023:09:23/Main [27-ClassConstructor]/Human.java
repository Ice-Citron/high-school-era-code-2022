
public class Human {

    String name;
    int age;
    double weight;

    Human(String name, int age, double weight) {

        this.name = name;
        this.age = age;
        this.weight = weight;

    }

    void eating() {
        System.out.printf("%s is eating.\n", this.name);
    }

}
