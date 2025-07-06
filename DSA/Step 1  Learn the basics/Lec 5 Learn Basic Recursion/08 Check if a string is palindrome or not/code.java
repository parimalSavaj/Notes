import java.util.Scanner;

public class code {

    public static Boolean reverseString(int i, String str) {
        if (i >= str.length() / 2) {
            return true;
        }

        if (str.charAt(i) != str.charAt(str.length() - i - 1)) {
            return false;
        }

        return reverseString(i + 1, str);
    }

    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter a string: ");
        String str = sc.nextLine();

        Boolean isPalindrome = reverseString(0, str);
        System.out.println("Is the string a palindrome? " + isPalindrome);
    }
}
