# Problem: Maximum Sub-Array Sum
#
# You are given an array of integers (positive, negative, or zero).
#
# Task:
# Find the maximum sum of any contiguous sub-Array.
#
# Notes:
# - Sub-Array must be continuous (no skipping elements)
# - You must pick at least one element
#
# Example:
# Input: [-2, 1, -3, 4, -1, 2, 1, -5, 4]
# Output: 6
# Explanation: Sub-Array [4, -1, 2, 1] gives sum = 6

def subArray(arr):
    max_sum = arr[0]
    for i in range(len(arr)):
        current_sum = 0
        for j in range(i,len(arr)):
            current_sum+=arr[j]

            if current_sum > max_sum:
                max_sum = current_sum
    
    return max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(f"output = {subArray(arr)}")

# TC O(n^2)
# SC O(1)