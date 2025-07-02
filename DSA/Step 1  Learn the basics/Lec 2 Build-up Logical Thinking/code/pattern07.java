import java.util.Scanner;

public class pattern07 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter n value: ");
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
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
