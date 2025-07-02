import java.util.Scanner;

public class pattern11 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        // for (int i = 0; i < n; i++) {
        // for (int j = 0; j <= i; j++) {
        // int number = (i + j) % 2 == 0 ? 1 : 0;
        // System.out.print(number);
        // }
        // System.out.println();
        // }

        int number = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print(number);
                number = 1 - number;
            }
            System.out.println();
        }
        sc.close();
    }
}
