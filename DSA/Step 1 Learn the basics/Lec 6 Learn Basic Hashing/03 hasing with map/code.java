import java.util.HashMap;
import java.util.Map;
import java.util.Scanner;

public class code {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        System.out.print("Enter number : ");
        int n = sc.nextInt();
        int arr[] = new int[n];
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 0; i < n; i++) {
            System.out.print("Enter value: ");
            int num = sc.nextInt();
            arr[i] = num;
            map.put(num, map.getOrDefault(num, 0) + 1);
        }

        System.out.println("Enter your number of numbers to find: ");
        int f = sc.nextInt();

        for (int i = 0; i < f; i++) {
            System.out.print("Enter value: ");
            int num = sc.nextInt();
            System.out.println(map.getOrDefault(num, 0));
        }

        sc.close();
    }

}
