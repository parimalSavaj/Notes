# If all the numbers in the array are twice, but one number is only once, then find that number.

# An array of integers
# Every number appears exactly twice
# Except one number, which appears only once

def findOnceNumOfArray(arr):
    num = 0

    for i in arr:
        num ^= i

    return num

arr = [1,1,2,2,3,4,4,5,5]

print(f"one is {findOnceNumOfArray(arr)}")

# TC O(n)
# SC O(1)