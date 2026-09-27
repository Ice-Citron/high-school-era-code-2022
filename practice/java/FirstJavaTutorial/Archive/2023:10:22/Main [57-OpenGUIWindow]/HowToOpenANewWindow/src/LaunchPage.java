import javax.sound.sampled.AudioSystem;
import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class LaunchPage implements ActionListener {

    JFrame frame = new JFrame();
    JButton myButton = new JButton();

    LaunchPage() {

        myButton.setBounds(200, 300, 200, 50);
        myButton.setFocusable(false);
        myButton.addActionListener(
            x -> {
                frame.dispose();
                System.out.println("Created a new window");
                NewWindow newWindow = new NewWindow();
            }
        );
        //myButton.addActionListener(this);

        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(new Dimension(600, 600));
        frame.setLayout(null);
        frame.add(myButton);

        frame.setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {

        if (e.getSource() == myButton) {
            NewWindow myWindow = new NewWindow();
        }

    }

}
