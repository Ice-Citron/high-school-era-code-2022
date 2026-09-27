
public class Vehicle {

    double speed = 0.0;

    Vehicle() {

    }

    void go() {
        System.out.printf("This vehicle is moving at %f kmh.\n", speed);
    }

    void stop() {
        System.out.println("This vehicle is now stopped.");
    }

}
