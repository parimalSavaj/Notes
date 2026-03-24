# left rotate array by one place.

# without any new array solve this problem.

def leftRotateArr(arr):
    if not arr:
        return

    temp = arr[0]
    for i in range(1,len(arr)):
        arr[i - 1] = arr[i]

    arr[len(arr) - 1] = temp;
    return arr
    
a = [1,2,3,4,5]

print(f"after rotate array look like {leftRotateArr(a)}")

# TC O(n)
# SC to use this problem is O(n)
# but SC to use extra is O(1)