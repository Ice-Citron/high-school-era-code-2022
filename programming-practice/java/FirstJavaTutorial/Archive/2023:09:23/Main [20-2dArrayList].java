
import java.util.*;

public class Main {
    public static void main(String[] args) {

        ArrayList<ArrayList<String>> groceryList = new ArrayList<>();

        ArrayList<String> foodList = new ArrayList<>();
        foodList.add("Chocalate");
        foodList.add("Hotdog");
        foodList.add("Squash");

        ArrayList<String> drinksList = new ArrayList<>();
        drinksList.add("Coke");
        drinksList.add("Slurpee");
        drinksList.add("100 plus");

        ArrayList<String> produceList = new ArrayList<>();
        produceList.add("Soda");
        produceList.add("Coke");

        groceryList.add(foodList);
        groceryList.add(drinksList);
        groceryList.add(produceList);

        System.out.println(groceryList.get(0).get(2));

    }
}
