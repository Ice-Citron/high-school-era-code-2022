import java.io.FileNotFoundException;
import java.io.FileReader;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {

        //FileReader = reads the contents of a file as a stream of characters. One by one
        //             read() returns an int valye which contains the byte value
        //             when read() returns -1, there is no more data to read

        try {
            FileReader reader = new FileReader("src/art.txt");
            int data = reader.read();
            while (data != -1) {
                System.out.print((char)data);
                data = reader.read();
            }
            reader.close();

        }
        catch (FileNotFoundException e) {
            e.printStackTrace();
        }
        catch (Exception e) {
            e.printStackTrace();
        }


    }
}
