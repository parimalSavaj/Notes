# check if array is sorted or not!

def checkSortedArray(arr):

    if not arr or len(arr) < 2:
        return;

    for i in range(0,len(arr)-1):
        if arr[i] <= arr[i+1]:
            continue
        else:
            return False
    return True

arr = [1,2,3,4,4,5] # True
arr = [1,2,4,3,5,6] # False
arr = [1] # None
print(f"given array is {checkSortedArray(arr)}")

# TC O(n)