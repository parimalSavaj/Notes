import java.util.Scanner;

public class pattern19 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            // star
            for (int j = i; j < n; j++) {
                System.out.print("*");
            }

            // space
            for (int j = 0; j < i * 2; j++) {
                System.out.print(" ");
            }

            // star
            for (int j = i; j < n; j++) {
                System.out.print("*");
            }
            System.out.println();
        }

        for (int i = n; i >= 0; i--) {
            // star
            for (int j = i; j < n; j++) {
                System.out.print("*");
            }

            // space
            for (int j = 0; j < i * 2; j++) {
                System.out.print(" ");
            }

            // star
            for (int j = i; j < n; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
    }
}
