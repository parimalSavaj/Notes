## Brute Force

- sorting the array and returning the last element.

## Better Approach

- no.

## Optimized Approach

- iterate through the array and keep track of the largest element using a if condition.

```java
int largest = arr[0];
for(int i = 0; i< arr.length; i++){
    if(arr[i] > largest){
        largest = arr[i];
    }
}
System.out.print("largest = " + largest);
```

## Time Complexity

- O(n)

## Space Complexity

- O(1)
