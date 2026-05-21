# Problem: Next Permutation
#
# You are given an array of numbers.
#
# Task:
# Rearrange numbers into the next greater permutation.
#
# Notes:
# - Next permutation means the next bigger arrangement
# - If no bigger permutation exists, return the smallest (sorted)
# - Must modify array in-place
#
# Example:
# Input: [1, 2, 3]
# Output: [1, 3, 2]
# Explanation: Next greater arrangement after [1,2,3] is [1,3,2]

def nextPermutation(arr):
    index = -1
    n = len(arr)

    for i in range(n - 2, -1, -1):
        if arr[i] < arr[i+1]:
            index=i
            break

    if index == -1:
        return arr[::-1]
    
    for i in range(n-1,index, -1):
        if arr[i] > arr[index]:
            arr[i], arr[index] = arr[index], arr[i]
            break
         
    arr[index+1:] = arr[index+1:][::-1]
    return arr


arr = [5,2,4,3,1]
print(nextPermutation(arr))