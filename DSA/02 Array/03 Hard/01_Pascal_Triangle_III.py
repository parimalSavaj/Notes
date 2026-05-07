# Pascal's Triangle:
# A triangular arrangement of numbers where:
# - Each row starts and ends with 1
# - Each middle element is the sum of the two elements above it
# - Row indexing starts from 0
# - Each row has (row + 1) elements
#
# Example:
# Row 0:         1
# Row 1:       1   1
# Row 2:     1   2   1
# Row 3:   1   3   3   1
# Row 4: 1   4   6   4   1
#
# Problem:
# Given a number N, print the first N rows of Pascal's Triangle.
#
# Example Input:
# N = 5
#
# Example Output:
# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1

def printPascalTriangle(n):
    if n <= 0:
        print("")
        return

    rows = n

    for row in range(0, rows):

        count = 1
        print(count, end=" ")

        for col in range(0, row):
            count = count * (row - col)
            count = count // (col + 1)

            print(count, end=" ")
        
        print()

printPascalTriangle(5)