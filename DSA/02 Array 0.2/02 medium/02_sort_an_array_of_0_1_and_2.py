# Problem: Sort an array of 0s, 1s, and 2s
#
# This is also known as the "Dutch National Flag Problem" (by Edsger W. Dijkstra).
#
# You are given an array that contains only three distinct values:
#   0, 1, and 2
#
# Your task is to rearrange the elements of the array such that:
#   - All 0s come first
#   - Then all 1s
#   - Then all 2s
#
# Example:
#   Input:  [2, 0, 1, 2, 1, 0]
#   Output: [0, 0, 1, 1, 2, 2]

def sortArray(arr):
    count0 = 0
    count1 = 0
    count2 = 0

    for i in arr:
        if i == 0:
            count0 += 1
        elif i == 1:
            count1 += 1
        else:
            count2 += 1
    
    for i in range(0, count0):
        arr[i] = 0
    
    for i in range(count0 + 1, count0 + count1):
        arr[i] = 1

    for i in range(count0+count1,len(arr)):
        arr[i] = 2

    return arr

arr = [2, 0, 1, 2, 1, 0]

print(f"after sorting look like {sortArray(arr)}")

# TC O(2n)
# SC O(n)