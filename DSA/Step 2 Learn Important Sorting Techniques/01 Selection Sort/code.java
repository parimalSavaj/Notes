public class code {
    public static void swap(int[] arr, int i, int j) {
        int temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }

    public static void main(String[] args) {
        int[] arr = { 5, 4, 2, 3, 1 };

        for (int i = 0; i < arr.length; i++) {
            int mini = i;
            for (int j = i; j < arr.length; j++) {
                if (arr[j] < arr[i]) {
                    mini = j;
                }
            }
            swap(arr, i, mini);
        }

        System.out.println("print array => ");

        for (int i = 0; i < arr.length; i++) {
            System.out.print(arr[i] + " ");
        }

    }
}