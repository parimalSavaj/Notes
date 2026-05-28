def checkSortedArr(arr):
    if not arr or len(arr) < 1:
        return None
    
    for i in range(1,len(arr)):
        if arr[i] < arr[i-1]:
            return False
    
    return True


# TC O(n)
# SC O(1)