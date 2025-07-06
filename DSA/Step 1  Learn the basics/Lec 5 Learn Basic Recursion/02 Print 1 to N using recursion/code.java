import java.util.Scanner;

public class code {

    public static void printN(int i, int n){
        if(i>n){
            return;
        }
        System.out.println(i);
        printN(i+1,n);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number: ");
        int n = sc.nextInt();

        printN(1,n);

        sc.close();
    }
}
