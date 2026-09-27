
import java.util.ArrayList;

public class Main {
    public static void main(String[] args) {

        String[] animals = {"cat", "dog", "parrot", "eagle", "duck"};

        for (String x : animals) {
            System.out.println(x);
        }

        ArrayList<String> arr = new ArrayList<>();
        arr.add("cat");
        arr.add("dogs");
        arr.add("parrot");

        for (String x : arr) {
            System.out.println(x);
        }

    }
}
