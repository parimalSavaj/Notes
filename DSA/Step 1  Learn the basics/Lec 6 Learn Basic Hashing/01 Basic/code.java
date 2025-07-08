import java.util.Scanner;

public class code {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter n value: ");
        int n = sc.nextInt();

        int arr[] = new int[n];

        int hashArr[] = new int[12];
        for (int i = 0; i < n; i++) {
            System.out.print("enter " + i + "value: ");
            int number = sc.nextInt();
            arr[i] = number;
            hashArr[number - 1] += 1;
        }

        System.out.print("Enter number of number you want to find: ");
        int findNum = sc.nextInt();
        for (int i = 0; i < findNum; i++) {
            System.out.print("Enter " + i + "value: ");
            int number = sc.nextInt();
            System.out.println("your number count is = " + hashArr[number - 1]);
        }

    }

}
