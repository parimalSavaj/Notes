# Problem: Leaders in an Array
#
# You are given an array of numbers.
#
# Task:
# Find all elements that are greater than or equal to
# all elements to their right side.
#
# Notes:
# - The last element is always a leader
# - Compare each element with elements on its right
# - Efficient approach is to traverse from right to left
# - Keep track of maximum element seen so far
#
# Example:
# Input: [16, 17, 4, 3, 5, 2]
# Output: [17, 5, 2]
# Explanation: These elements are greater than all elements to their right

def leadersArr(arr):
    max_number = float('-inf') # we find negative array values as well. 
    leaders_array = []

    for i in reversed(arr):
        if max_number < i:
            leaders_array.append(i)
            max_number = i

    # return leaders_array[::-1] # if proper order want
    return leaders_array


# arr = [16, 17, 4, 3, 5, 2]
arr = [-5, -2, -10]

print(leadersArr(arr))

# TC O(n)
# SC O(k)