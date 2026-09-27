
public class Student {

    private String name;
    private int age;
    private String major;
    private int grade;

    Student(String name, int age, String major, int grade) {
        this.name = name;
        this.age = age;
        this.major = major;
        this.grade = grade;
    }

    public String getName() { return this.name; }
    public void setName(String name) { this.name = name;}

    public int getAge() { return this.age; }
    public void setAge(int age) { this.age = age; }

    public String getMajor() { return this.major; }
    public void setMajor(String major) { this.major = major; }

    public int getGrade() { return this.grade; }
    public void setGrade(int grade) { this.grade = grade; }

}
