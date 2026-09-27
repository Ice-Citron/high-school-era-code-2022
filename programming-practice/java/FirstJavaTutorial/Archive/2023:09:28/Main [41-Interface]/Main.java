
public class Main {
    public static void main(String[] args) {

        //interface = a template that can be applied to a class.
        //            simillar to inheritance, but specifies what a class has/must do.
        //            classes can apply more than one inheritance, however inheritance is limited to 1 direct superclass (parent)

        Rabbit rabbit = new Rabbit();
        Hawk hawk = new Hawk();
        Fish fish = new Fish();

        rabbit.flee();
        hawk.hunt();
        fish.flee();


    }
}
