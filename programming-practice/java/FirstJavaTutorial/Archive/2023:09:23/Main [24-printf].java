
public class Main {
    public static void main(String[] args) {

        // % [flags] [precision] [width] [conversion character]

        // [conversion-character]
        System.out.printf("This is a format string %d\n", 123);
        System.out.printf("This is a format float %f\n", 22.03f);
        System.out.printf("This is a format double %f\n", 22.03f);
        System.out.printf("This is a format boolean %b\n", true);
        System.out.printf("This is a format float %c\n", 'c');
        System.out.printf("This is a format double %s\n", "he he he haw");

        // [width]
        // minimum number of characters to be written as output
        String name = "yumin lee";
        System.out.printf("Hello %12s\n", name);

        // [precision]
        // set the number of digit, when outputting floating point or double values
        System.out.printf("The value of pi is: %.4f\n", 3.14159263f);

        // [flags]
        // adds an effect to output, based on the flag added to format justifier
        // - : left-justify (string is printed to very left, if allocated space > string itself)
        // + : outputs the magnitude of numeric value, such as '+' for positive, and '-' for negative
        // 0 : numeric values are zero padded
        // , : comma grouping separator number, if value > 1000
        System.out.printf("Hello %-12s. Welcome back!\n", name);
        System.out.printf("The value of numeria is %+.5f\n", -21.58291628);
        System.out.printf("The value of numeria is %+020.5f\n", -21.58291628);
        System.out.printf("The value of 1 million is %,+020.6f\n", 1000000.124567831);
    }
}
