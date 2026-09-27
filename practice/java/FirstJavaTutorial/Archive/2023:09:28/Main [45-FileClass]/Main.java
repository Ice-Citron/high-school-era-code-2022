import java.io.File;

public class Main {
    public static void main(String[] args) {

        File file = new File("src/random.txt");

        if (file.exists()) {
            System.out.println("The file exists!");
            System.out.println(file.getPath());
            System.out.println(file.getAbsolutePath());
            System.out.println(file.isFile());      //verify if path leads to a file or a folder
            file.delete();
        }
        else {
            System.out.println("The file doesn't exists!");
        }

    }
}
