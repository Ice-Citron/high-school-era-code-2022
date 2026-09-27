import javax.swing.*;

public class Main {
    public static void main(String[] args) {

        //JOptionPane = pops up a standard dialog box that prompts users for a value
        //              or informs them of something.

        /**
         * The 'null' is parent_components
        JOptionPane.showMessageDialog(null, "This is some useless information.", "title", JOptionPane.PLAIN_MESSAGE);
        JOptionPane.showMessageDialog(null, "Here is more useless information", "title", JOptionPane.INFORMATION_MESSAGE);
        JOptionPane.showMessageDialog(null, "really? do you have to do this?", "title", JOptionPane.QUESTION_MESSAGE);
        JOptionPane.showMessageDialog(null, "YOUR COMPUTER HAS VIRUS!", "title", JOptionPane.WARNING_MESSAGE);
        JOptionPane.showMessageDialog(null, "CALL TECH SUPPORT NOW OR ELSE!!", "title", JOptionPane.ERROR_MESSAGE);

        int answer = JOptionPane.showConfirmDialog(null, "bro do you even code?", "title", JOptionPane.YES_NO_CANCEL_OPTION);
        String name = JOptionPane.showInputDialog("What is your name?");
        **/

        String[] responses = {"No, you're awesome!", "Thank you!", "*Blushes*"};
        ImageIcon icon = new ImageIcon("src/flag.png");

        JOptionPane.showOptionDialog(
                null, "You are awesome", "Title - Secret Message",
                JOptionPane.YES_NO_CANCEL_OPTION,
                JOptionPane.INFORMATION_MESSAGE,
                icon,
                responses,
                0
                );


    }
}
