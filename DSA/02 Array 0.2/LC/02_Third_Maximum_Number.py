# Problem: Find the third distinct maximum number in an array

# Goal:
# - Return the 3rd DISTINCT maximum number
# - If it does not exist, return the maximum number

# Key concept:
# - DISTINCT means unique values only
# - Duplicate values should be counted once

# Example 1:
# nums = [3, 2, 1]
# Distinct values → [3, 2, 1]
# 1st max = 3
# 2nd max = 2
# 3rd max = 1
# Output = 1

# Example 2:
# nums = [1, 2]
# Distinct values → [2, 1]
# Only 2 distinct numbers exist
# No 3rd maximum → return the maximum
# Output = 2

# Example 3:
# nums = [2, 2, 3, 1]
# Distinct values → [3, 2, 1]
# Note: duplicate 2 is counted once
# 3rd max = 1
# Output = 1

# Important observations:
# - Remove duplicates first OR ignore them while processing
# - You only need top 3 distinct numbers
# - If total distinct numbers < 3 → return max

# Constraints:
# - Array size up to 10^4
# - Values can be large (negative and positive)

# Optimization idea:
# - Aim for O(n) time (single pass)
# - Track top 3 distinct values while iterating

# Approach hint:
# - Use three variables: first, second, third max
# - Update them while iterating through the array
# - Skip numbers already seen (avoid duplicates)

class Solution(object):
    def thirdMax(self, nums):
        first = second = third = None

        for num in nums:
            if num == first or num == second or num == third:
                continue

            if first is None or num > first:
                third = second
                second = first
                first = num
            elif second is None or num > second:
                third = second
                second = num
            elif third is None or num > third:
                third = num

        return third if third is not None else first