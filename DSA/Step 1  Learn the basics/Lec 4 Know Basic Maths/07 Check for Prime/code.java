import java.util.Scanner;

public class code {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your number: ");
        int num = sc.nextInt();

        int count = 0;
        for (int i = 1; i * i <= num; i++) {
            if (num % i == 0) {
                count++;
                if ((num / i) != i) {
                    count++;
                }
            }
        }

        if (count == 2) {
            System.out.println("number is prime");
        } else {
            System.out.println("Number is not prime");
        }
    }
}
