# Two Sum Problem - Understanding the Question

# You are given:
# 1. A list (array) of integers called 'nums'
#    Example: nums = [2, 7, 11, 15]
#
# 2. A target integer called 'target'
#    Example: target = 9

# Your task:
# Find TWO DIFFERENT elements in the array such that:
# nums[i] + nums[j] == target

# Important:
# - You must pick two different indices (i != j)
# - You cannot use the same element twice
# - Each input usually has exactly one valid answer

# What to return:
# - Return the INDICES (positions) of those two numbers
# - Not the actual numbers, but their positions in the list

# Example:
# nums = [2, 7, 11, 15]
# target = 9
#
# Explanation:
# nums[0] = 2
# nums[1] = 7
# 2 + 7 = 9  --> matches target
#
# Output:
# [0, 1]

# In short:
# Find two different positions in the array
# where the sum of their values equals the target.

def twoSum(arr, target):
    lookup = {}

    for i in range(0,len(arr)):
        secondNumber = target - arr[i]

        if secondNumber in lookup:
            return [lookup[secondNumber], i]

        lookup[arr[i]] = i
    return []

arr = [4,1,2,3,1]
target = 5

print(f"output = {twoSum(arr,target)}")

# TC O(n)
# SC O(n)