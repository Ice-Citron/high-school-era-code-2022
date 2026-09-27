
public class Person {

    String name;
    int age;

    Person() {

    }

    Person(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String toString() {
        return name + " " + age;
    }

}
