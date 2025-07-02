import java.util.Scanner;

public class pattern13 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter N value: ");
        int n = sc.nextInt();

        int number = 1;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j <= i; j++) {
                System.out.print(number);
                System.out.print(" ");
                number++;
            }
            System.out.println();
        }
        sc.close();
    }
}
