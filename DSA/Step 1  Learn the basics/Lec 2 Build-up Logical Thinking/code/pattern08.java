import java.util.Scanner;

public class pattern08 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        for (int i = n; i > 0; i--) {
            // space
            for (int j = i; j < n; j++) {
                System.out.print(" ");
            }

            // star
            for (int j = 1; j < i * 2; j++) {
                System.out.print("*");
            }

            System.out.println();
        }
        sc.close();
    }
}
