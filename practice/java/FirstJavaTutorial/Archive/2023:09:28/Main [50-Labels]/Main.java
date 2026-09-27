
import javax.swing.*;
import java.awt.*;
import javax.swing.ImageIcon;
import javax.swing.border.Border;


public class Main {
    public static void main(String[] args) {

        //MyFrame frame = new MyFrame();
        ImageIcon image = new ImageIcon("src/cat.png");
        Border border = BorderFactory.createLineBorder(Color.green, 10);

        //check whether image exists
        if (image.getImageLoadStatus() == MediaTracker.ERRORED) {
            System.out.println("Failed to load the image!");
        }
        else {
            System.out.println("Image loaded successfully.");
        }

        //JLabel = a GUI display area for a string of text, an image, or both.

        JLabel label = new JLabel(); //create a label
        label.setText("Hello world Jaemus!"); //set text of label
        label.setIcon(image);

        label.setHorizontalTextPosition(JLabel.CENTER);  //set text's horizontal position, [LEFT, CENTER, RIGHT] of ImageIcon
        label.setVerticalTextPosition(JLabel.TOP);  //set text's vertical position, [TOP, CENTER, BOTTOM] of ImageIcon

        label.setForeground(Color.green);    //alternatively (new Color(0x00FF00))
        label.setFont(new Font("Arial", Font.PLAIN, 20));
        label.setIconTextGap(15); //sets gap of text to image
        label.setBackground(Color.black); //set background colour
        label.setOpaque(true); //need to set to True in order for background colour to be visible
        label.setBorder(border); //running the green border initialised

        label.setVerticalAlignment(JLabel.CENTER); //set vertical position of icon+text within label
        label.setHorizontalAlignment(JLabel.CENTER); //set horizontal position of icon+text within label
        label.setBounds(0, 0, 250, 250); //set x, y position within frame, as well as dimensions

        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 500);
        //frame.setLayout(null);
        frame.add(label);
        frame.pack();
        frame.setVisible(true);

    }
}


