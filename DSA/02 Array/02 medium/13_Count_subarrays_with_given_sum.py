# Problem: Count subarrays with given sum
#
# You are given an array of integers and a target sum k.
# Your task is to count how many continuous subarrays have a sum equal to k.
#
# A subarray means a contiguous part of the array (elements must be next to each other).
#
# Example:
#   Input:  nums = [1, 2, 3], k = 3
#   Output: 2
#
# Explanation:
#   There are two subarrays whose sum is equal to 3:
#     - [1, 2]
#     - [3]
#
# The goal is simply to identify all such contiguous subarrays
# and count how many satisfy the condition (sum == k).

def count_subarrays(nums, k):
    prefix_map = {0: 1}
    current_sum = 0
    count = 0

    for num in nums:
        current_sum += num

        if (current_sum - k) in prefix_map:
            count += prefix_map[current_sum - k]

        prefix_map[current_sum] = prefix_map.get(current_sum, 0) + 1

    return count