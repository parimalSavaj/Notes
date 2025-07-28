import java.util.Scanner;

public class code {

    public static void printSum(int n,int sum){
        if(n<1){
            System.out.println(sum);
            return;
        }
        printSum(n-1,sum+n);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number: ");
        int n = sc.nextInt();

        printSum(n,0);

        sc.close();
    }
}
