import java.util.Scanner;

public class code {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter your full string : ");
        String str = sc.next();
        int hashArr[] = new int[26];

        for (int i = 0; i < str.length(); i++) {
            hashArr[str.charAt(i) - 'a'] += 1;
        }

        for (int i = 0; i < hashArr.length; i++) {
            char currentChar = (char) ('a' + i);
            System.out.println(currentChar + " " + hashArr[i]);
        }
        sc.close();
    }

}
