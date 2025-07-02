import java.util.Scanner;

public class code {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter Number : ");
        int num = sc.nextInt();

        int copyNumber = num;
        int armstrongNumber = 0;

        // first count length of this number
        int temp = num;
        int length = 0;
        while (temp > 0) {
            length++;
            temp /= 10;
        }

        while (num > 0) {
            int digit = num % 10;
            armstrongNumber += Math.pow(digit, length);
            num /= 10;
        }

        System.out.println(armstrongNumber == copyNumber);
    }
}
