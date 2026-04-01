# Problem: Majority Element-I
#
# Given an array of size n, find the element that appears **more than** n/2 times.
#
# A majority element is the one that occurs more than half of the array size.
#
# Example:
#   Input:  [2, 2, 1, 2, 3]
#   Output: 2   (appears more than n/2 times)

def majorityElement(arr):
    hashMap = {}

    for num in arr:
        hashMap[num] = hashMap.get(num, 0) + 1

    maxNum = 0
    keyNum = None

    for key, val in hashMap.items():
        if val > maxNum:
            maxNum = val
            keyNum = key

    if maxNum > len(arr) // 2:
        return keyNum
    
arr = [2, 2, 1, 2, 3]

print(majorityElement(arr))

# TC O(2n)
# SC O(n)