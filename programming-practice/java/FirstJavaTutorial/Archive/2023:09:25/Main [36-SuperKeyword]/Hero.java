
public class Hero extends Person {

    String power;

    Hero(String name, int age, String power) {
        //super.name = name;
        //super.age = age;
        super(name, age);
        this.power = power;
    }

    @Override
    public String toString() {
        return super.toString() + " " + this.power;
    }

}
