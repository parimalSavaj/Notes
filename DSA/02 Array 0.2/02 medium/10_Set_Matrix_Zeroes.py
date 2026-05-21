# Problem: Set Matrix Zeroes
#
# You are given a matrix.
#
# Task:
# If any element is 0, make its entire row and column 0.
#
# Simple Explanation:
# - Whenever you see a 0, that row and column must become 0
# - But if you change values immediately, you may create extra zeros by mistake
# - So first remember which rows and columns need to be zero
# - Then update the matrix based on that
#
# Example:
# Input:
# [
#   [1, 1, 1],
#   [1, 0, 1],
#   [1, 1, 1]
# ]
#
# Output:
# [
#   [1, 0, 1],
#   [0, 0, 0],
#   [1, 0, 1]
# ]
#
# Key Point:
# - One zero affects its whole row and column

def matrixZero(arr, n,m):
    row = [0] * n
    col = [0] * m

    for i in range(0,n):
        for j in range(0,m):
            if arr[i][j] == 0:
                row[i] = 1
                col[j] = 1
    
    for i in range(0,n):
        for j in range(0,m):
            if row[i] or col[j]:
                arr[i][j] = 0

    
arr = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]

matrixZero(arr, 3, 3)
print(arr)

# TC O(2 × n × m)
# SC O(n + m)

# have not optimal solution but it's ok for me