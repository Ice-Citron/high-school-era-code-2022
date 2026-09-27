import javax.swing.*;
import java.awt.*;

public class Main {
    public static void main(String[] args) {

        //Layout Manager = Defines the natural layout for components within a container

        //Flow layout = places component in a row, sized at their preferred size.
        //              If the horizontal space in the container is too small
        //              the FlowLayout class uses the next available row

        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(500, 500);
        frame.setLayout(new FlowLayout(FlowLayout.CENTER, 10, 10));

        JPanel panel = new JPanel();
        panel.setPreferredSize(new Dimension(350, 250));
        panel.setBackground(Color.lightGray);
        panel.setLayout(new FlowLayout(FlowLayout.CENTER, 0, 0));

        panel.add(new Button("1"));
        panel.add(new Button("2"));
        panel.add(new Button("3"));
        panel.add(new Button("4"));
        panel.add(new Button("5"));
        panel.add(new Button("6"));
        panel.add(new Button("7"));
        panel.add(new Button("8"));
        panel.add(new Button("9"));
        panel.add(new Button("10"));

        frame.add(panel);
        frame.setVisible(true);
    }
}
