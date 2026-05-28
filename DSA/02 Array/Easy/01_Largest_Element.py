def largestElement(arr):
    if not arr:
        return
    
    largest = arr[0]
    for num in arr:
        if num > largest:
            largest = num
    
    return largest

arr = [3, 7, 2, 9, 5]

print(largestElement(arr))

# TC O(n)
# SC O(1)