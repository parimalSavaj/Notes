## 02 Second Largest Element

- here second condition jovani

## 04 Remove duplicates from sorted array

- two pointer method.
- put 'i' inside start and check with 'j' if not same so +i and value of j stored into new +1 place.

## 05 left rotate array by K places

#### better

- first store K'th element of array inside temp array
- then this K'th element to end move to first using condition

```
    for i in range(k,n):
        arr[i-k] = arr[i]
```

- then temp store element put in last pace using condition

```
    for i in range(n-k,n):
        arr[i] = temp[i-(n-k)]
```

#### optimal

- here main logic is Reversal Logic
- then call three time 0 to k -1, then k to n - 1 and final 0 to n - 1
