import java.util.Scanner;

public class code {

    public static void printN(int n){
        if(n<1){
            return;
        }
        System.out.println(n);
        printN(n-1);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number: ");
        int n = sc.nextInt();

        printN(n);
        sc.close();
    }
}
