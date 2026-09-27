import javax.swing.ImageIcon;
import javax.swing.JFrame;
import java.awt.*;

public class MyFrame extends JFrame {

    MyFrame() {

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setResizable(false);
        this.setTitle("JFrame Label");
        this.setSize(420, 420);
        this.setVisible(true);

        ImageIcon image = new ImageIcon("src/cat.png");
        this.setIconImage(image.getImage());
        this.getContentPane().setBackground(new Color(0x0FE0A0));

        /*
        if (image.getImageLoadStatus() == MediaTracker.ERRORED) {
            System.out.println("Failed to load the image!");
        } else {
            System.out.println("Image loaded successfully.");
        }
         */
    }

}
