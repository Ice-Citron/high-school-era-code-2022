
public class Main {
    public static void main(String[] args) {

        System.out.println(add(1, 5, 21));

    }

    private static int add(int a, int b) {
        System.out.println("This is overloaded method #1");
        return a + b;
    }

    private static int add(int a, int b, int c) {
        System.out.println("This is overloaded method #2");
        return a + b + c;
    }

    private static int add(int a, int b, int c, int d) {
        System.out.println("This is overloaded method #3");
        return a + b + c + d;
    }

}
