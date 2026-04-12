# Problem: Check if an array is monotonic

# Definition:
# An array is monotonic if it is either:
# - Monotone increasing OR
# - Monotone decreasing

# Monotone increasing:
# For all i <= j → nums[i] <= nums[j]
# (elements stay same or increase)

# Monotone decreasing:
# For all i <= j → nums[i] >= nums[j]
# (elements stay same or decrease)

# Goal:
# - Return True if array is monotonic
# - Otherwise return False

# Example 1:
# nums = [1, 2, 2, 3]
# Always increasing (allow equal values)
# Output = True

# Example 2:
# nums = [6, 5, 4, 4]
# Always decreasing (allow equal values)
# Output = True

# Example 3:
# nums = [1, 3, 2]
# Goes up (1 → 3) then down (3 → 2)
# Not monotonic
# Output = False

# Key observations:
# - Equal values are allowed
# - Only one direction should exist (up OR down)
# - If direction changes → not monotonic

# Approach idea:
# - Track direction (increasing or decreasing)
# - Iterate through array once
# - If both increasing and decreasing found → return False

# Constraints:
# - Array size up to 100000
# - Values can be negative or positive

# Optimization:
# - Solve in O(n) time (single pass)
# - Use simple comparisons between adjacent elements

class Solution(object):
    def isMonotonic(self, nums):
        inc = dec = True

        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                dec = False
            elif nums[i] < nums[i - 1]:
                inc = False

        return inc or dec