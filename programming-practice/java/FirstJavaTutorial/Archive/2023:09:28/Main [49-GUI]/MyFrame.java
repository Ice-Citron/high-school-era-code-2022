
import javax.swing.*;
import java.awt.*;

public class MyFrame extends JFrame {

    MyFrame() {

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //Exit out of application when pressed 'X' button
        this.setResizable(false); //prevents frame from being resized
        this.setTitle("JFrame Title"); // sets title of frame
        this.setSize(420, 420); //sets t he x-dimension and y-dimension of the frame
        this.setVisible(true); //make frame visible

        ImageIcon image = new ImageIcon("cat.png"); //creates an image icon
        this.setIconImage(image.getImage()); //changes icon of frame
        this.getContentPane().setBackground(new Color(0x0FE0A0));

    }

}
