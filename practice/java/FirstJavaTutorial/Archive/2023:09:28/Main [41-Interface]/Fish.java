
public class Fish implements Prey, Predator{

    Fish() {

    }

    @Override
    public void flee() {
        System.out.println("This fish is fleeing from a larger fish.");
    }

    @Override
    public void hunt() {
        System.out.println("This fish is hunting a smaller fish.");
    }

}
