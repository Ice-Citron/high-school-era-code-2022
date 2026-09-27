import java.io.FileWriter;
import java.io.IOException;

public class Main {
    public static void main(String[] args) {

        try {
            FileWriter writer = new FileWriter("src/poems.txt");
            writer.write("Roses are red\nViolets are blue\nqwertyuiop");
            writer.append("\nhello world");
            writer.close();
        }
        catch (IOException e) {
            e.printStackTrace();
        }

    }
}
