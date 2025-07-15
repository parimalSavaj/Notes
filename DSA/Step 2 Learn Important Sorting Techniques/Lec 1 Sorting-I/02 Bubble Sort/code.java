public class code {
    public static void main(String[] args) {
        int[] arr = { 5, 4, 3, 2, 1 };

        for (int i = arr.length; i > 1; i--) {
            boolean hasNotSwap = true;
            for (int j = 0; j < i - 1; j++) {
                if (arr[j] > arr[j + 1]) {
                    int temp = arr[j];
                    arr[j] = arr[j + 1];
                    arr[j + 1] = temp;

                    hasNotSwap = false;
                }
            }
            if (hasNotSwap) {
                break;
            }
        }

        System.out.println("print arr => ");

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }
    }
}
