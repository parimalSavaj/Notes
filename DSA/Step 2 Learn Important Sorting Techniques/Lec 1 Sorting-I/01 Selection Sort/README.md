## selection sort

**figure out minimum, and swap with first( or it's current position )**

> **`🧠`**

1. swap happen on index 0 to maximum index of array.
2. swap happen on index 1 to maximum index of array.
3. go on...

```java
for (int i = 0; i < arr.length; i++) {
    int mini = i;
    for (int j = i; j < arr.length; j++) {
        if (arr[j] < arr[i]) {
            mini = j;
        }
    }
    swap(arr, i, mini);
}
```

- time complexity => O(n^2) [ based on code is best, average and worst ]
