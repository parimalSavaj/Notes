import java.util.Scanner;

public class code {

    public static void printFibonacci(int i, int j, int n) {
        if (i > n) {
            return;
        }
        System.out.println(i + " ");
        printFibonacci(j, i + j, n);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter you number : ");
        int n = sc.nextInt();

        printFibonacci(0, 1, n);

        sc.close();
    }
}
