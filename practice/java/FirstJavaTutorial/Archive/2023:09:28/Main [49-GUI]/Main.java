import javax.swing.ImageIcon;
import javax.swing.JFrame;
import java.awt.Color;

public class Main {
    public static void main(String[] args) {

        /*
        //Jframe = a GUI window to add components to

        JFrame frame = new JFrame(); //creates a frame

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); //Exit out of application when pressed 'X' button
        //frame.setDefaultCloseOperation(JFrame.HIDE_ON_CLOSE); //Hide window when pressed 'X' button
        //frame.setDefaultCloseOperation(JFrame.DO_NOTHING_ON_CLOSE); //Do nothing when pressed 'X' button
        frame.setResizable(false); //prevents frame from being resized
        frame.setTitle("JFrame Title"); // sets title of frame
        frame.setSize(420, 420); //sets t he x-dimension and y-dimension of the frame
        frame.setVisible(true); //make frame visible

        ImageIcon image = new ImageIcon("cat.png"); //creates an image icon
        frame.setIconImage(image.getImage()); //changes icon of frame
        //frame.getContentPane().setBackground(Color.green);
        //frame.getContentPane().setBackground(new Color(128, 64, 32));
        frame.getContentPane().setBackground(new Color(0x0FE0A0));
        */
        MyFrame myFrame = new MyFrame();
    }
}
