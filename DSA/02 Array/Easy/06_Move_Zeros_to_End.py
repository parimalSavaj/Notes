# Problem:
# Given an array/list of integers, move all 0s to the end of the array.
#
# Requirements:
# - Non-zero elements should remain in their original relative order.
# - Perform the modification on the same array if possible.
#
# Example:
# Input : [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]
#
# Example:
# Input : [1, 2, 3]
# Output: [1, 2, 3]
#
# Example:
# Input : [0, 0, 0]
# Output: [0, 0, 0]

def moveZerosToEnd(arr):
    if not arr:
        return

    i = 0

    for j in range(0,len(arr)):
        if arr[j] != 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
    
    return arr


# TC: O(n)
# SC: O(1)


