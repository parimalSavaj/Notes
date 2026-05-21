# Problem: Rotate Matrix by 90 Degrees
#
# You are given a 2D square matrix (n x n).
# Each element represents a value at a specific row and column.
#
# Task:
# Rotate the matrix by 90 degrees (clockwise).
#
# Notes:
# - The matrix is square (same number of rows and columns)
# - Rotation should be done in-place (modify the original matrix [optional] )
# - Do not use extra space for another matrix (unless specified otherwise)
#
# Example:
# Input:
# [
#   [1, 2, 3],
#   [4, 5, 6],
#   [7, 8, 9]
# ]
#
# Output:
# [
#   [7, 4, 1],
#   [8, 5, 2],
#   [9, 6, 3]
# ]

def rotateMatrix(arr):
    n = len(arr)

    rotatedMatrix = [[0]*n for _ in range(n)]

    for i in range(n):
        for j in range(n):
            rotatedMatrix[j][n-1-i] = arr[i][j]

    return rotatedMatrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = rotateMatrix(matrix)

print(result)