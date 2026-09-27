
public class Main {
    public static void main(String[] args) {

        String[][] cars = {
                {"Camaro", "Ford", "Mercedes"},
                {"Camaro1", "Ford1", "Mercedes1"},
                {"Camaro2", "Ford2", "Mercedes2"},
                };  //initialiser used

        for (int i = 0; i < cars.length; ++i) {
            for (int j = 0; j < cars.length; ++j) {
                System.out.println(cars[i][j]);
            }
        }


    }
}
