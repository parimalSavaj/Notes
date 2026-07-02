# Problem: Find Missing Number
#
# You are given an array containing distinct numbers from a sequence.
# The sequence should contain all numbers within a specific range,
# but exactly one number is missing.
#
# Your task is to identify and return the missing number.
#
# Example:
# Input: [3, 0, 1]
# Output: 2


#*############################
#!        sum method
#*############################
def findMissingNumberUsingSumMethod(arr,n):
    totalSum = n * (n + 1) // 2
    sum = 0
    for i in arr:
        sum += i
    
    return totalSum - sum

