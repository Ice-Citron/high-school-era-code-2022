
public class Main {
    public static void main(String[] args) {

        Car car1 = new Car("Toyota", "Supra", 2012);
        Car car2 = new Car("Ford", "Mustang", 2008);
        Car car3 = new Car(car1);

        System.out.printf("%s, %s, %s \n", car3.getMake(), car3.getModel(), car3.getYear());

    }
}
