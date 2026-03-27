# maximum consecutive ones

# An array consisting of only 0s and 1s
# Your task:
# Find the maximum number of consecutive (continuous) 1s in the array.

def maxContinuousOnes(arr):
    count = 0
    maxCount = 0

    for i in arr:
        if i == 1:
            count += 1
            maxCount = max(count,maxCount)
        else:
            count = 0

    return maxCount

arr = [1,1,0,1,1,1,0,1,1]

print(f"inside array maximum 1 is {maxContinuousOnes(arr)}")