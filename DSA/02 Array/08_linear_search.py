# Linear search on array.

def linearSearch(arr, ch):
    if not arr:
        return -1
    for i in range(0,len(arr)):
        if arr[i] == ch:
            return i

    return -1 

arr = [1,5,4,2,3]

index = linearSearch(arr,7)
if index == -1:
    print(f"your number not found")
else:
    print(f"you number found at {index} index and number is {arr[index]}")

# TC O(n)
# SC O(1)