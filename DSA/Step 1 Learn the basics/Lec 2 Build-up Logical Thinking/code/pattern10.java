import java.util.Scanner;

public class pattern10 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter N value: ");
        int n = sc.nextInt();

        for (int i = 1; i < n * 2; i++) {
            // calculation
            int star = i > n ? 2 * n - i : i;
            for (int j = 1; j <= star; j++) {
                System.out.print("*");
            }
            System.out.println();
        }
        sc.close();
    }
}
