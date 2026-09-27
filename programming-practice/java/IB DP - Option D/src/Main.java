
public class Main {
    public static void main(String[] args) {

        Node treeRoot = new Node(50);
        Node leaf1 = new Node(25);
        Node leaf2 = new Node(75);
        Node leaf3 = new Node(19);
        Node leaf4 = new Node(27);
        Node leaf5 = new Node(78);
        Node leaf6 = new Node(21);

        treeRoot.left = leaf1;
        treeRoot.right = leaf2;

        leaf1.left = leaf3;
        leaf1.right = leaf4;

        leaf2.right = leaf5;
        leaf3.right = leaf6;

        outputTree(treeRoot);
        findMinimum(treeRoot);
    }

    public static void outputTree(Node root) {
        if (root == null) {
            return;
        }
        outputTree(root.left);
        outputTree(root.right);
        System.out.printf("%d ", root.data);
    }

    public static int findMinimum(Node root) {
        if (root.left == null) {
            return root.data;
        }
        else {
            return findMinimum(root.left);
        }

    }

}
