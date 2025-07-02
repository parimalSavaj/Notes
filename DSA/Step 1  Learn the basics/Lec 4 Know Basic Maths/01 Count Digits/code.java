import java.util.Scanner;

public class code {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter N value: ");
        int num = sc.nextInt();
        int count = 0;

        while (num > 0) {
            num = num / 10;
            count++;
        }
        System.out.println("Your count is : " + count);
    }
}
