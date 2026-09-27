import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MyFrame extends JFrame implements ActionListener {

    JButton myButton = new JButton("Submit");
    JTextField textField = new JTextField();

    MyFrame() {

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        //this.setSize(600, 600);
        this.setLayout(new FlowLayout());


        //myButton.addActionListener(this);
        myButton.addActionListener(
            x -> {
                textField.setEditable(false);
                myButton.setEnabled(false);
                System.out.printf("Welcome back %s!\n", textField.getText());
            }
        );

        textField.setPreferredSize(new Dimension(250, 40));
        textField.setFont(new Font("Arial", Font.PLAIN, 30));
        textField.setForeground(new Color(0x00FF00));
        textField.setBackground(Color.black);
        textField.setCaretColor(Color.white);
        textField.setText("Username");
        //textField.setEditable(true);

        this.add(textField);
        this.add(myButton);
        this.pack(); //used to size the JFrame automatically to the size of the widgets within the page
        this.setVisible(true);
    }

    @Override
    public void actionPerformed(ActionEvent e) {
        textField.setEditable(false);
        myButton.setEnabled(false);
        System.out.printf("Welcome back %s!\n", textField.getText());
    }

}
