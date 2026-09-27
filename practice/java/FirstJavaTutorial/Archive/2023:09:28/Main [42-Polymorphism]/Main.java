
public class Main {
    public static void main(String[] args) {

        //polymorphism = greek word, "poly" means many, and "morph-" means form
        //               The ability of an object to identify as more than one type.

        Car car = new Car();
        Bicycle bicycle = new Bicycle();
        Boat boat = new Boat();

        Vehicle[] racers = {car, bicycle, boat};
        Object[] racer2 = {car, bicycle, boat}; //all objects are also children classes of the 'Object' superclass

        for (Vehicle x : racers) {
            x.go();
        }

    }
}
