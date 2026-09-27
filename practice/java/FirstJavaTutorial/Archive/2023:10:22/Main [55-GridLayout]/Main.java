import javax.swing.*;
import java.awt.*;

public class Main {
    public static void main(String[] args) {

        //Layout Manager = Defines the natural layout for components within a container

        //Grid Layout = places the components in a grid of cells.
        //              Each component takes all the available space within its cell,
        //              and each cell is the same size

        JFrame frame = new JFrame();
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(new Dimension(600, 600));
        frame.setLayout(new GridLayout(3, 3, 0, 0));

        frame.add(new Button("1"));
        frame.add(new Button("2"));
        frame.add(new Button("3"));
        frame.add(new Button("4"));
        frame.add(new Button("5"));
        frame.add(new Button("6"));
        frame.add(new Button("7"));
        frame.add(new Button("8"));
        frame.add(new Button("9"));


        frame.setVisible(true);
    }
}
