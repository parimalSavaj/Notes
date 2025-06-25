import java.util.Scanner;

public class pattern22 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        for (int i = 1; i < n * 2; i++) {
            for (int j = 1; j < n * 2; j++) {
                int top = j - 1;
                int left = i - 1;
                int bottom = (n * 2) - j - 1;
                int right = (n * 2) - i - 1;

                int min = Math.min(Math.min(top, bottom), Math.min(left, right));
                System.out.print(n - min);
            }
            System.out.println();
        }
    }
}
