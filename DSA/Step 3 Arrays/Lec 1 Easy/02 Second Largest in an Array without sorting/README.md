## Brute Force

- sort the array and return the second last element.

## Better Approach

- iterate through the array and keep track of the largest,

- next iterate through the array and keep track of the second largest element using a if condition not equal to the largest element but greater than the second largest element.

## Optimized Approach

- iterate through the array and keep track of the largest and second largest element using a if condition.

```java
int largest = arr[0];
int secondLargest = -1;
for(int i = 0; i< arr.length; i++){
    if(arr[i] > largest){
        secondLargest = largest;
        largest = arr[i];
    } 
    if(arr[i] > secondLargest && arr[i] != largest){
        secondLargest = arr[i];
    }
}
```

## Time Complexity

- O(n)

## Space Complexity

- O(1)
