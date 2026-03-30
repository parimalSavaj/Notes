# Longest sub array with given sum K(positives)

# Given an array of positive integers and a target value **K**, the task is to find the **longest sub array** whose sum is exactly equal to **K**.

# A **sub array** is a continuous sequence of elements within the array (elements must be next to each other, without skipping any).

# Among all possible sub arrays whose sum equals **K**, you need to consider the one with the **maximum length** (i.e., the highest number of elements).

# **In simple terms:**
# Find the longest continuous part of the array such that the sum of its elements is equal to **K**.

# we solve using two pointers

def longestSubArrayWithSumK(arr, k):
    left = 0
    total = 0
    maxLen = 0

    for right in range(len(arr)):
        total += arr[right]

        # Shrink window if sum exceeds k
        while total > k and left <= right:
            total -= arr[left]
            left += 1

        # Check if sum equals k
        if total == k:
            maxLen = max(maxLen, right - left + 1)

    return maxLen

# TC O(2n)
# SC O(1)