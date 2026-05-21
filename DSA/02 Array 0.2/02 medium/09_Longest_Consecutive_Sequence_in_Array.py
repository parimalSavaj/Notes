# Problem: Longest Consecutive Sequence in an Array
#
# You are given an array of numbers.
#
# Task:
# Find the length of the longest sequence of consecutive numbers.
#
# Notes:
# - Consecutive means numbers follow each other (x, x+1, x+2, ...)
# - The sequence does NOT need to be in order in the array
# - Duplicates should be ignored
# - Efficient approach uses a set for O(1) lookup
#
# Example:
# Input: [100, 4, 200, 1, 3, 2]
# Output: 4
# Explanation: Longest consecutive sequence is [1, 2, 3, 4]

def longestConsecutiveArr(arr):
    if not arr:
        return 0

    arr.sort()
    
    longestCount = 1
    currentLength = 1
    lastMinNum = arr[0]

    for i in arr[1:]:
        if i == lastMinNum:
            continue
        elif i == lastMinNum + 1:
            currentLength += 1
        else:
            currentLength = 1

        lastMinNum = i
        longestCount = max(longestCount, currentLength)

    return longestCount

arr = [100, 4, 200, 1, 3, 2]

print(longestConsecutiveArr(arr))

# TC O(n lon n)
# SC O(k)