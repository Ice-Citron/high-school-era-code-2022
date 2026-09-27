import javax.swing.*;
import java.awt.*;

public class NewWindow {

    JFrame frame = new JFrame();
    Label label = new Label("Hello World!");

    NewWindow() {

        label.setBounds(0, 0, 150, 50);
        label.setFont(new Font(null, Font.PLAIN, 20));

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(new Dimension(300, 300));
        frame.setLayout(null);

        frame.add(label);
        frame.setVisible(true);

    }

}
