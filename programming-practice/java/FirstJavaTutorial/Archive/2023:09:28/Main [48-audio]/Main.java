import javax.sound.sampled.*;
import java.io.IOException;
import java.io.File;
import java.util.Locale;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws UnsupportedAudioFileException, IOException, LineUnavailableException {

        Scanner scanner = new Scanner(System.in);

        File file = new File("src/We live we love we lie.wav");
        AudioInputStream audioStream = AudioSystem.getAudioInputStream(file);
        Clip clip = AudioSystem.getClip();
        clip.open(audioStream);

        String response = "";

        while (!response.equals("Q")) {
            System.out.println("P = Play | S = Stop | R = Restart | Q = Quit");
            System.out.println("Enter your choice: ");

            response = scanner.next();
            response = response.toUpperCase();

            switch(response) {
                case "P":
                    clip.start();
                    break;
                case "S":
                    clip.stop();
                    break;
                case "R":
                    clip.setMicrosecondPosition(0);
                    break;
                case "Q":
                    clip.close();
                    break;
                default:
                    System.out.println("Not a valid response.");
            }
        }
        System.out.println("Audio playback stopped!");

    }
}
