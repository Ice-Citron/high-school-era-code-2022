import javax.swing.*;
import javax.swing.border.Border;
import java.awt.*;

public class Main {
    public static void main(String[] args) {

        //JPanel = A GUI component that functions as a container to hold other componenets

        ImageIcon icon = new ImageIcon("src/cat.jpeg");
        JLabel label = new JLabel();
        label.setText("Hello world");
        label.setIcon(icon);

        label.setVerticalAlignment(JLabel.CENTER);
        label.setHorizontalAlignment(JLabel.CENTER);      //don't need to set vertical and horizontal allignment when using no layout manager
                                                          //this is something to use when using a border layout
        //label.setBounds(0, 0, 200, 200);

        if (icon.getImageLoadStatus() == MediaTracker.ERRORED) {
            System.out.println("Failed to load the image!");
        }
        else {
            System.out.println("Image loaded successfully.");
        }

        JPanel redPanel = new JPanel();
        redPanel.setBackground(Color.red);
        redPanel.setBounds(0, 0, 250, 250);     //x-cord, y-cord, width, height
        redPanel.setLayout(new BorderLayout());
        //redPanel.setLayout(null);
        redPanel.add(label);

        JPanel bluePanel = new JPanel();
        bluePanel.setBackground(Color.blue);
        bluePanel.setBounds(250, 0, 250, 250);
        bluePanel.setLayout(new BorderLayout());

        JPanel greenPanel = new JPanel();
        greenPanel.setBackground(Color.green);
        greenPanel.setBounds(0, 250, 250, 250);
        greenPanel.setLayout(new BorderLayout());

        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(null);
        frame.setSize(720, 720);
        frame.setVisible(true);
        frame.add(redPanel);
        frame.add(bluePanel);
        frame.add(greenPanel);
        frame.pack();




    }
}
