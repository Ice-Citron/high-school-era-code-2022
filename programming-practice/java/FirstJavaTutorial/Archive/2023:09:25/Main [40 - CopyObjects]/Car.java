
public class Car {

    String make;
    String model;
    int year;

    Car() {

    }

    Car(Car car) {
        this.copy(car);
    }

    Car(String make, String model, int year) {
        this.make = make;
        this.model = model;
        this.year = year;
    }

    public String getMake() { return this.make; }
    public String getModel() { return this.model; }
    public int getYear() { return this.year; }

    public void setMake(String make) { this.make = make; }
    public void setModel(String model) { this.model = model; }
    public void setYear(int year) { this.year = year; }

    //Copy object function
    public void copy(Car car) {
        this.setMake(car.getMake());
        this.setModel(car.getModel());
        this.setYear(car.getYear());
    }

}
