def dominantIndex(self, nums):
    if not nums:
        return -1

    largestNum = nums[0]
    lergestNumInx = 0
    secondLargestNum = float('-inf')

    for i in range(0,len(nums)):
        if nums[i] > largestNum:
            secondLargestNum = largestNum
            largestNum = nums[i]
            lergestNumInx = i

        if secondLargestNum < nums[i] and largestNum > nums[i]:
            secondLargestNum = nums[i]

    if (secondLargestNum * 2) > largestNum:
        return -1
    else:
        return lergestNumInx