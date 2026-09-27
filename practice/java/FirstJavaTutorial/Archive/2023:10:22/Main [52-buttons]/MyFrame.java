
import javax.swing.*;
import javax.swing.plaf.ActionMapUIResource;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class MyFrame extends JFrame implements ActionListener {

    JButton button = new JButton();
    JLabel label = new JLabel();

    MyFrame() {

        ImageIcon icon = new ImageIcon("src/cat.jpeg");
        ImageIcon icon2 = new ImageIcon("src/square.png");

        label.setIcon(icon2);
        label.setBounds(150, 250, 150, 150);
        label.setVisible(false);

        button.setBounds(325, 100, 200, 50);
        //button.addActionListener(this);

        //Alternative with using Lambda functions
        button.addActionListener(
                x -> {
                    System.out.println("Hello world.");
                    button.setEnabled(false);
                    label.setVisible(true);
                }
        );
        button.setText("I am a button.");
        button.setFocusable(false);
        button.setIcon(icon);
        button.setHorizontalTextPosition(JButton.CENTER);
        button.setVerticalTextPosition(JButton.CENTER);
        button.setFont(new Font("Arial", Font.BOLD, 20));
        button.setIconTextGap(-15);
        button.setForeground(Color.cyan); //changes colour of font
        button.setBackground(Color.lightGray); //changes colour of button background
        button.setBorder(BorderFactory.createEtchedBorder());
        //button.setEnabled(false); //this disables a button

        this.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        this.setLayout(null);
        this.setSize(850, 550);
        this.setVisible(true);

        this.add(button);
        this.add(label);
    }

    @Override
    public void actionPerformed(ActionEvent e){

        if (e.getSource() == button) {
            //System.out.println("The button is pressed");
        }
    }

}
