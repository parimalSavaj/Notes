# Problem: Traverse Matrix in Spiral Order
#
# You are given a 2D matrix.
# You need to read all elements in a spiral manner.
#
# Spiral means moving in a circular pattern:
#   - First go left → right (top row)
#   - Then go top → bottom (right column)
#   - Then go right → left (bottom row)
#   - Then go bottom → top (left column)
#
# After one round, move inside and repeat the same steps.
#
# Example:
#   Input:
#   1   2   3   4   5
#   6   7   8   9  10
#  11  12  13  14  15
#  16  17  18  19  20
#  21  22  23  24  25
#
#   Output:
#   1 2 3 4 5 10 15 20 25 24 23 22 21 16 11 6 7 8 9 14 19 18 17 12 13
#
# Idea:
#   Think of the matrix as layers.
#   First cover outer layer, then inner layer.
#
# Spiral Order Output:
#   1  2  3  4  5
#  10 15 20 25
#  24 23 22 21
#  16 11  6
#   7  8  9
#  14 19
#  18 17
#  12
#  13
#
# Important:
#   - Visit each element only once
#   - Continue until all elements are covered

def spiralOrder(matrix):
    if not matrix:
        return []

    result = []
    top, bottom = 0, len(matrix) - 1
    left, right = 0, len(matrix[0]) - 1

    while top <= bottom and left <= right:

        for i in range(left, right + 1):
            result.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            result.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                result.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(matrix[i][left])
            left += 1

    return result

# TC O(n*m)
# SC O(1)