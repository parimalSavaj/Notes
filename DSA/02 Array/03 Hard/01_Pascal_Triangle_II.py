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
# Given a row number (r),
# return all the elements present in that row of Pascal's Triangle.
#
# Example Input:
# r = 4
#
# Example Output:
# [1, 4, 6, 4, 1]
#
# Explanation:
# Row 4 in Pascal's Triangle contains 5 elements:
# [1, 4, 6, 4, 1]

def printPascalRow(row):
    if row == 0 :
        print(1)
        return
    
    count = 1
    print(count)

    for i in range(0,row):
        count = count * (row - i)
        count = count // (i + 1)
        print(count)

printPascalRow(4)