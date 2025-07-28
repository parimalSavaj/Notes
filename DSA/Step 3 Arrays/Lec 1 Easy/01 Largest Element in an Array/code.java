public class code {
    public static void main(String[] args) {
        int[] arr = { 1, 2, 3, 6, 5, 4, 0 };

        int largest = arr[0];

        for (int i = 0; i < arr.length; i++) {
            if (arr[i] > largest) {
                largest = arr[i];
            }
        }

        System.out.println("largest = " + largest);
    }
}
