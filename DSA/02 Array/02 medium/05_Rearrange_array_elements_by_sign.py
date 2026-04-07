# Rearrange Array Elements by Sign
# --------------------------------
# Given an array of integers containing both positive and negative numbers,
# rearrange the elements so that they appear alternately by sign.
#
# That means:
# positive, negative, positive, negative, ...
#
# Notes:
# - "Rearrange" means change positions, NOT sort the array.
# - "By sign" means based on positive (+) and negative (-) values.
#
# Example:
# Input:  [1, 2, -3, -1, -2, 3]
# Output: [1, -3, 2, -1, 3, -2]
#
# Important points (depending on question variation):
# - The number of positive and negative elements may be equal or unequal.
# - If unequal, extra elements go at the end.
# - Sometimes order must be preserved (stable), sometimes not required.
#
# Goal:
# Arrange elements so positives and negatives alternate.

# def rearrangeBySign(arr):
    
#     pos = []
#     neg = []
    
#     for num in arr:
#         if num > 0:
#             pos.append(num)
#         else:
#             neg.append(num)
    
#     n = len(arr)
#     result = [0] * n   # ✅ pre-allocate
    
#     for i in range(len(pos)):  # assuming equal count
#         result[2*i] = pos[i]
#         result[2*i + 1] = neg[i]
    
#     return result

# TC O(2n)
# SC O(n)
#! this solution can not for old number of element inside array.

def rearrangeBySign(arr):
    n = len(arr)
    result = [0]*n

    posIndex = 0
    negIndex = 1

    for num in arr:
        if num > 0:
            result[posIndex] = num
            posIndex += 2
        else:
            result[negIndex] = num
            negIndex += 2

    return result
    

arr = [1, 2, -3, -1, -2, 3, 4]
print(rearrangeBySign(arr))

# TC O(n)
# SC O(n)