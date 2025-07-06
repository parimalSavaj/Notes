import java.util.Scanner;

public class code {

    public static void printName(int i,int n){
        if(i>n){
            return;
        }
        System.out.println("Parimal");
        printName(i+1,n);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number of times you want to print the name: ");
        int n = sc.nextInt();

        printName(1,n);
        sc.close();
    }

    // Time Complexity: O(n)
    // Space Complexity: O(n)
}
