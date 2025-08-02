## check if array is sorted.

- Loop through the array, and for every element arr[i], check whether it is greater than the next element arr[i + 1].

```java
for (int i = 1; i < arr.length; i++) {
        if (arr[i] < arr[i - 1]) {
            return false;
        }
    }
    return true;
```

## Time Complexity

- O(n)

## Space Complexity

- O(1)
