## 02 Second Largest Element

- here second condition jovani

## 04 Remove duplicates from sorted array

- two pointer method.
- put 'i' inside start and check with 'j' if not same so +i and value of j stored into new +1 place.

## 05 left rotate array by K places

#### better

- first store K'th element of array inside temp array `temp = arr[:k]`

- then this K'th element to last element of array move to first using condition

```
    for i in range(k,n):    # condition k'th element to last element
        arr[i-k] = arr[i]
```

- then temp's element put in last

```
    for i in range(n-k,n):
        arr[i] = temp[i-(n-k)]
```

#### optimal

- here main logic is Reversal Logic
- then call three time 0 to k - 1, then k to n - 1 and final 0 to n - 1

#### for right rotation!

- first rotate full array 0 to n - 1
- then first k'th element 0 to k - 1
- and then remening k to n - 1

## 06 Move Zeros to End

- here first put one pinter 'i' in to 0 index.
- then start running loop with 'j'
- and 'j' value check `if 'j' value is not 0` so `swap` this value

## 07 Union of two sorted arrays

- first prepare variable, length of both array and 'i' & 'j' pointer and unionArr
- then while loop for length of `i < n1 and j < n2`
  - inside this loop get small value using condition `arr1[i] < arr2[j]`, second elif `arr2[j] < arr1[i]` and same value using `arr1[i] == arr[j]`
  - then inside main condition to check first value of unionArr and last element of unionArr is not this element.
    - `if not unionArr or unionArr[-1] != arr1[i]` for arr1[i] < arr2[j]
    - `if not unionArr or unionArr[-1] != arr2[j]` for arr2[j] < arr1[i]
    - `if not unionArr or unionArr[-1] != arr1[i]` for arr1[i] == arr2[j]
- using above logic only one array end and loop over
- so for remaining any array we want to write single single while with if condition

## 08 Find missing number

- main logic is first N number sum formula `n * (n + 1) // 2`
- then run loop on given array and sum them
- in last minus Total sum with array sum, and we get missing number.
