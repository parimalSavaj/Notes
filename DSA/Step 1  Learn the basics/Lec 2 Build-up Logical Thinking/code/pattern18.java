import java.util.Scanner;

public class pattern18 {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        for (int i = n; i > 0; i--) {
            char ch = (char) ('A' + i - 1);
            for(int j = 0; j <= n - i; j++ ){
                System.out.print(ch);
                ch++;
            }
            System.out.println();
        }
    }
}
