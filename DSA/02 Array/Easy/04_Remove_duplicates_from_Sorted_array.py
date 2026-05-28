def removeDuplicates(arr):
    if not arr:
        return None
    
    i = 0

    for j in range(1,len(arr)):
        if arr[i] != arr[j]:
            i += 1
            arr[i] = arr[j]

    return i+1

# TC O(n)
# SC O(1)