
import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Stack;

public class Main {

    public static void main(String[] args) {
        /*
        LinkedList<Student> studentList = new LinkedList<>();

        Student student1 = new Student("John Doe", 20, "Computer Science", 85);
        Student student2 = new Student("James Murray", 17, "Sport Science", 65);

        studentList.add(student1);
        studentList.add(student2);
        studentList.add(new Student("Jolie Teo", 17, "Physics", 77));
        studentList.add(new Student("Yumin Lee", 21, "Biology", 87));
        studentList.add(new Student("Chen Ding", 22, "Chemistry", 33));

        studentList.remove(1); //studentList.remove(student2); - this removes by object
                               //studentList.removeLast();

        //displayStudentInfo(studentList);

        Student[] testArr = {
                new Student("Jolie Teo", 17, "Physics", 77), new Student("Avelyn Lim", 17, "Physics", 77),
                new Student("Yumin Lee", 17, "Physics", 77), new Student("Joanna", 17, "Physics", 77)
        };
        //displayStudentInfo(arrayToLinkedList(testArr));
        //displayStudentArray(linkedListToArray(studentList));

        //displayStudentArray(forwardIterator_linkedListToArray(studentList));
        //displayStudentArray(reverseIterator_linkedListToArray(studentList));

        //displayStudentInfo(iterator_removeByName(studentList, "Jolie Teo"));
        //displayStudentInfo(removeByName(studentList, "Jolie Teo"));

        int[][] testAllocation = new int[5][5];
        int[][] grades = {
                {1, 2, 3, 4, 5},
                {1, 2, 3, 4, 5},
                {1, 2, 3, 4, 5},
                {1, 2, 3, 4, 5},
                {1, 2, 3, 4, 5}
        };

        displayGrades(grades);
        */

        /*
        Stack<Student> studentStack = new Stack<Student>();
        studentStack.push(new Student("Jolie Teo", 17, "Physics", 77));
        studentStack.push(new Student("Yumin Lee", 21, "Biology", 87));
        studentStack.push(new Student("Chen Ding", 22, "Chemistry", 33));
        studentStack.add(new Student("Avelyn Lim", 17, "Aeronautics", 77));
        studentStack.add(new Student("Amann Li", 21, "Yoga", 87));
        studentStack.add(new Student("Jason Chen", 22, "Sport Science", 33));

        //displayStack(studentStack);
        //System.out.println(studentStack);

        Stack<Integer> stack = new Stack<>();
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(1);
        stack.push(2);
        stack.push(3);
        stack.push(4);
        stack.push(3);
        stack.push(2);



        System.out.println(stack);
        removeFromStack(stack, 3);
        System.out.println(stack);

        */
        
        System.out.println(factorial(5));
        System.out.println(power(3, 5));
        String s = "hello world";
        System.out.println(s.substring(1, 11));
        System.out.println(isPalindrome("NiggereggiN"));

        recursionDemonstrator(5);

    }

    public static int factorial(int n) {
        if (n == 0) {
            return 1;
        }
        //System.out.printf("%d\n", n);
        return factorial(n-1) * n;
    }

    public static int power(int base, int exponents) {
        if (exponents == 0) { return 1; }
        if (base == 0) { return 1; }
        return base * power(base, exponents - 1);
    }

    public static boolean isPalindrome(String word) {
        if (word.length() <= 1) { return true; }
        if (word.charAt(0) == word.charAt(word.length() - 1)) {
            return isPalindrome(word.substring(1, word.length() - 1));
        }
        else {
            return false;
        }
    }

    public static void recursionDemonstrator(int n) {
        if (n != 0) {
            System.out.printf("%d ", n);
            recursionDemonstrator(n - 1);
            System.out.printf("%d ", n);
        }
    }

    /*
    public static void displayStack(Stack<Student> stack) {
        for (int i = 0; i < stack.size(); i++) {
            Student temp = stack.get(i);
            System.out.printf("%s %d %s %d\n", temp.getName(), temp.getAge(), temp.getMajor(), temp.getGrade());
        }
    }

    public static void removeFromStack(Stack<Integer> stack, int removeValue) {
        Stack<Integer> temp = new Stack<Integer>();
        while (!stack.isEmpty()) {
            int i = stack.pop();
            if (i != (Integer)removeValue) {
                temp.push(i);
            }
        }
        while (!temp.isEmpty()) {
            stack.push(temp.pop());
        }
    }

    public static void removeLoopStack(Stack<Integer> stack, int removeValue) {
        for (int i = 0; i < stack.size();) {
            if (stack.get(i) == (Integer)removeValue ) { stack.remove(i); }
            else { i++; }
        }
    }
    */

    /*

    public static void displayStudentInfo(LinkedList<Student> studentList) {
        for (int i = 0; i < studentList.size(); i++) {
            System.out.printf("%s ", studentList.get(i).getName()); //gets the Student object, then retreives name via getter
            System.out.printf("%d ", studentList.get(i).getAge());
            System.out.printf("%s ", studentList.get(i).getMajor());
            System.out.printf("%d \n", studentList.get(i).getGrade());
        }
    }

    public static void displayStudentArray(Student[] arr) {
        for (int i = 0; i < arr.length; i++) {
            Student student = arr[i];
            System.out.printf("%s %d %s %d\n", student.getName(), student.getAge(), student.getMajor(), student.getGrade());
        }
    }

    public static LinkedList<Student> arrayToLinkedList(Student[] array) {
        LinkedList<Student> studentList = new LinkedList<>();
        for (int i = 0; i < array.length; i++) {
            studentList.add(array[i]);
        }
        return studentList;
    }

    public static Student[] linkedListToArray(LinkedList<Student> studentList) {
        Student[] array = new Student[studentList.size()];
        for (int i = 0; i < studentList.size(); i++) {
            array[i] = studentList.get(i);
        }
        return array;
    }

    public static Student[] forwardIterator_linkedListToArray(LinkedList<Student> studentList) {
        ListIterator<Student> studentIterator = studentList.listIterator();
        Student[] arr = new Student[studentList.size()];
        int i = 0;
        while (studentIterator.hasNext()) {
            arr[i] = studentIterator.next();
            i++;
        }
        return arr;
    }

    public static Student[] reverseIterator_linkedListToArray(LinkedList<Student> studentList) {
        //the .size() is to start the iterator at 1 past the last value in the student list
        ListIterator<Student> studentIterator = studentList.listIterator(studentList.size());
        Student[] arr = new Student[studentList.size()];
        int i = 0;
        while(studentIterator.hasPrevious()) {
            arr[i] = studentIterator.previous();
            i++;
        }
        return arr;
    }

    //Find and remove element from LinkedList
    public static LinkedList<Student> iterator_removeByName(LinkedList<Student> studentList, String studentName) {
        ListIterator<Student> studentIterator = studentList.listIterator();
        while (studentIterator.hasNext()) {
            if (studentIterator.next().getName() == studentName) {
                studentIterator.remove();
            }
        }
        return studentList;
    }

    public static LinkedList<Student> removeByName(LinkedList<Student> studentList, String studentName) {
        for (int i = 0; i < studentList.size(); i++) {
            if (studentList.get(i).getName() == studentName) {
                studentList.remove(i);
            }
        }
        return studentList;
    }

    public static void displayGrades(int[][] arr) {
        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                System.out.printf("%d ", arr[i][j]);
            }
            System.out.println();
        }
    }
    */
}