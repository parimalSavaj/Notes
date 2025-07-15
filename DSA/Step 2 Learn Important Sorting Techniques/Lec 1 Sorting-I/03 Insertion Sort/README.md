## Insertion Sort

**iterate one by one ans sort them at current position**

> **`🧠`**

1. step 1:

- here only one element so not sort.

2. step 2:

- now first and second have two element so sort them.

- same go up to end.

```java
for (int i = 0; i < arr.length; i++) {
    int j = i;
    while (j > 0 && arr[j - 1] > arr[j]) {
        int temp = arr[j];
        arr[j] = arr[j - 1];
        arr[j - 1] = temp;

        j--;
    }
}
```

- time complexity => O(n^2) [ based on code is average and worst ]
- time complexity => O(n) [ based on code is best ]
