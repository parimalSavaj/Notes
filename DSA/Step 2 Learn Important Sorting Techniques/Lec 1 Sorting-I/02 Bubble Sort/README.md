## Bubble Sort

**iterate every two pair and get maximum and put into last ( adjacent swap )**

> **`🧠`**

1.

- first and second get max and put it in second place.
- now second and third index and get max and put in to third place.
- same up-to last. ( that for only first time so we get at last max number. )

2.

- same up-to step 1 but now start from second and third not first...

```java
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
```

- time complexity => O(n^2) [ based on code is average and worst ]
- time complexity => O(n) [ based on code is best ]
