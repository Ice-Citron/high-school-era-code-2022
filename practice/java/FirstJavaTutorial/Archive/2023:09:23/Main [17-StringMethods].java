
public class Main {
    public static void main(String[] args){

        String test = "Bro";

        System.out.println(test.equals("Bro"));             //(boolean) test if "Bro" equals to "Bro"
        System.out.println(test.equalsIgnoreCase("bro"));   //(boolean) test if "Bro" is equalled to "bro", nonetheless of capital casing
        System.out.println(test.length());                  //(int)     outputs the length of "Bro"
        System.out.println(test.charAt(2));                 //(char)    prints the 3rd character 'o'
        System.out.println(test.indexOf('r'));              //(int)     prints out index of 'r' - 1
        System.out.println(test.isEmpty());                 //(boolean) test if "test" variable is empty
        System.out.println(test.toUpperCase());             //(string)  outputs "Bro" into "BRO"
        System.out.println(test.toLowerCase());

        String trail = "   Yumin   Lee     ";

        System.out.println(trail.trim());                   //(string)  outputs trail with all of its spaces on very left and right removed.
        System.out.println(trail.replace('e', 'a').trim()); //(string)  replaces all 'e' chars in Yumin Lee to 'a' and trim

    }
}
