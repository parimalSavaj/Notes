import java.util.Scanner;

public class pattern03 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("enter n value: ");
        int n = sc.nextInt();

        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print(j + 1);
            }
            System.out.println();
        }
    }
}