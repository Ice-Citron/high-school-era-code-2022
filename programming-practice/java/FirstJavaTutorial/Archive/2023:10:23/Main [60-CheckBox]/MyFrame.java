import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MyFrame extends JFrame implements ActionListener {

    JButton button = new JButton();
    JCheckBox checkBox = new JCheckBox();
    ImageIcon xIcon = new ImageIcon("src/x.jpeg");
    ImageIcon checkIcon = new ImageIcon("src/check.jpeg");

    MyFrame() {

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLayout(new FlowLayout());

        button.setText("Submit");
        //button.addActionListener(this);
        button.addActionListener(
            x -> {
                System.out.printf("%b\n", checkBox.isSelected());
            }
        );

        checkBox.setText("I am not a robot.");
        checkBox.setFocusable(false);
        checkBox.setFont(new Font("Arial", Font.PLAIN, 22));

        //Setting the true and false icons of checkbox to images
        checkBox.setIcon(xIcon);
        checkBox.setSelectedIcon(checkIcon);

        this.add(button);
        this.add(checkBox);

        this.pack();
        this.setVisible(true);

    }

    @Override
    public void actionPerformed(ActionEvent e) {
        System.out.printf("%b\n", checkBox.isSelected());
    }
}
