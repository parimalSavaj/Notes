import java.util.Scanner;

public class code {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter N value: ");
        int num = sc.nextInt();

        int duplicateNumber = num;
        int reverseNumber = 0;

        while (num > 0) {
            reverseNumber = (reverseNumber * 10) + num % 10;
            num = num / 10;
        }

        System.out.println(duplicateNumber == reverseNumber);
        sc.close();
    }
}
