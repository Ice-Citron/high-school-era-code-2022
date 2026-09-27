
public class Main {
    public static void main(String[] args) {

        //super = keyword refers to the superclass (parent) of an object
        //        very simillar to the "this" keyword

        Hero hero = new Hero("Batman", 42, "$$$");
        //System.out.printf("Hero: %s %d %s\n", hero.name, hero.age, hero.power);
        System.out.println(hero.toString());
    }
}
