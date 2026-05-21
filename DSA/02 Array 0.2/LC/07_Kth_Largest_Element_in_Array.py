import random

def findKthLargest(nums, k):
    target = len(nums) - k

    def quickselect(left, right):
        pivot = nums[right] 
        i = left 

        for j in range(left, right):
            if nums[j] <= pivot:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        nums[i], nums[right] = nums[right], nums[i]

        if i == target:
            return nums[i]
        elif i < target:
            return quickselect(i + 1, right)
        else:
            return quickselect(left, i - 1)

    return quickselect(0, len(nums) - 1)
