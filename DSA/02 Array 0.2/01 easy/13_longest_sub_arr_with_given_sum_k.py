# Longest sub array with given sum K(positives)

# Given an array of positive integers and a target value **K**, the task is to find the **longest sub array** whose sum is exactly equal to **K**.

# A **sub array** is a continuous sequence of elements within the array (elements must be next to each other, without skipping any).

# Among all possible sub arrays whose sum equals **K**, you need to consider the one with the **maximum length** (i.e., the highest number of elements).

# **In simple terms:**
# Find the longest continuous part of the array such that the sum of its elements is equal to **K**.

def longestSubArrayWithSumK(arr, k):
    preSumMap = {}
    total_sum = 0
    maxLen = 0

    for i in range(len(arr)):
        total_sum += arr[i]

        # If sum itself equals k
        if total_sum == k:
            maxLen = max(maxLen, i + 1)

        # Remaining sum
        rem = total_sum - k

        # Check if rem exists in map
        if rem in preSumMap:
            length = i - preSumMap[rem]
            maxLen = max(maxLen, length)

        if total_sum not in preSumMap: # This condition ensures the code works for both positive and negative numbers
            preSumMap[total_sum] = i

    return maxLen

# this is better solution for positive

# TC O(n)
# SC O(n)