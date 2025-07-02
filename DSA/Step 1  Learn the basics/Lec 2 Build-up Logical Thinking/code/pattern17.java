import java.util.Scanner;

public class pattern17 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        for (int i = 1; i <= n; i++) {
            // space
            for (int j = n; j > i; j--) {
                System.out.print(" ");
            }

            // charter
            char ch = 'A';
            for (int j = 1; j < i * 2; j++) {
                System.out.print(ch);
                if (i > j) {
                    ch++;
                } else {
                    ch--;
                }
            }
            System.out.println();
        }
    }
}
