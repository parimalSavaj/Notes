# Problem: Find a Peak Element in an array

# A peak element is an element that is greater than its neighbors
# For index i:
# nums[i] > nums[i-1] and nums[i] > nums[i+1]

# Edge cases:
# First element is a peak if nums[0] > nums[1]
# Last element is a peak if nums[n-1] > nums[n-2]

# Key points:
# - There can be multiple peak elements
# - You can return ANY one peak
# - You do NOT need the maximum element
# - The array is NOT sorted

# Intuition:
# Think of the array like a mountain ⛰️
# Example: [1, 3, 5, 4, 2]
# You go up: 1 → 3 → 5
# Then go down: 5 → 4 → 2
# The highest point (5) is a peak

# Another example:
# [1, 2, 1, 3, 5, 6, 4]
# Peaks are:
# - 2 (greater than neighbors 1 and 1)
# - 6 (greater than neighbors 5 and 4)
# You can return index of either peak

# Important insight:
# - If you are moving upward, a peak must exist ahead
# - If you are moving downward, a peak must exist behind

# What to return:
# - Return the INDEX of any peak element
# - Not the value, only the position

# Goal:
# - Try to solve better than brute force
# - This problem is commonly solved using binary search

class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :return type: int
        """

        left,right = 0, len(nums) - 1

        while left < right:
            mid = (left+right) // 2

            if nums[mid] > nums[mid+1]:
                right = mid
            else:
                left = mid + 1

        return left


        