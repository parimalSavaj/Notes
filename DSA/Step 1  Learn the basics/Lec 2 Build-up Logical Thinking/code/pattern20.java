import java.util.Scanner;

public class pattern20 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            // star
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }

            // space
            int space = (n - i) * 2;
            for (int j = 0; j < space; j++) {
                System.out.print(" ");
            }

            // star
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
        for (int i = n; i >= 1; i--) {
            // star
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }

            // space
            int space = (n - i) * 2;
            for (int j = 0; j < space; j++) {
                System.out.print(" ");
            }

            // star
            for (int j = 1; j <= i; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
