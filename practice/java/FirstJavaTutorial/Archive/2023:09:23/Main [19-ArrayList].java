
import java.util.ArrayList;

public class Main {
    public static void main(String[] args){

        //ArrayList - a resizable array, elements can be added and removed after compilation phase
        //            stores reference data types

        ArrayList<Character> arr = new ArrayList<>();

        arr.add('A');
        arr.add('B');
        arr.add('D');
        arr.add('E');

        arr.set(2, 'Z');
        arr.remove(3);
        arr.clear();

        for (int i = 0; i < arr.size(); ++i) {
            System.out.println(arr.get(i));
        }

    }
}
