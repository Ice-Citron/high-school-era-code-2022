
public class Main {
    public static void main(String[] args) {

        Human human = new Human("Jia yao", 21, 55.00);
        System.out.println(human.name + human.age + human.weight);
        human.eating();
    }
}
