# Problem: Peak Index in a Mountain Array
#
# You are given a "mountain" array, which means:
#   - Elements strictly increase up to one point (peak)
#   - Then strictly decrease after that point
#
# Your task is to return the index of the peak element.
#
# In simple words:
#   - Find the position of the highest number in the array
#
# Example:
#   Input:  [1, 3, 5, 4, 2]
#   Output: 2
#   Explanation: 5 is the peak element, and its index is 2.
#
# Note:
#   - The array always has exactly one peak
#   - Length of array is at least 3

def peakIndexInMountainArray(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        left,right = 0, len(arr) - 1

        while left < right:
            mid = (left+right) // 2

            if arr[mid] > arr[mid+1]:
                right = mid
            else:
                left = mid + 1

        return left