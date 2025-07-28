import java.util.Scanner;

public class code {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter number : ");
        int n = sc.nextInt();

        // for (int i = 1; i <= n; i++) {
        // if (n % i == 0) {
        // System.out.print(i + ", ");
        // }
        // }

        for (int i = 1; i * i <= n; i++) {
            if (n % i == 0) {
                System.err.println(i);
                if (n / i != i) {
                    System.out.println(n / i);
                }
            }
        }
        sc.close();
    }
}
