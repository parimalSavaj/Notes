import java.util.Scanner;

public class code {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number 1 : ");
        int num1 = sc.nextInt();
        System.out.print("Enter number 2 : ");
        int num2 = sc.nextInt();

        int GCD = 1;
        /*
         * method 1
         * time => O(min(num1, num2))
         */
        // for (int i = 1; i <= Math.min(num1, num2); i++) {
        // if (num1 % i == 0 && num2 % i == 0) {
        // GCD = i;
        // }
        // }

        /*
         * method 2
         * time => O(min(num1, num2))
         * this code best case is very good based on method 1
         */
        // for (int i = Math.min(num1, num2); i >= 1; i--) {
        // if (num1 % i == 0 && num2 % i == 0) {
        // GCD = i;
        // break;
        // }
        // }

        /*
         * method 3 [ Euclid algorithm]
         * see image.md
         * GCD of (num1, num2) = GCD of (num1 % num2, num2) [num2 > num1]
         * time => O(log ∅ min(num1, num2))
         */

        while (num1 > 0 && num2 > 0) {
            if (num1 > num2) {
                num1 = num1 % num2;
            } else {
                num2 = num2 % num1;
            }
        }
        if (num1 == 0) {
            GCD = num2;
        } else {
            GCD = num1;
        }
        System.out.println("GCD = " + GCD);
        sc.close();
    }
}
