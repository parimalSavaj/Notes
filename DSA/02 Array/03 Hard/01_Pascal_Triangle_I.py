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
# Given a row number (r) and column number (c),
# find the value at that position in Pascal's Triangle.
#
# Example Input:
# r = 4, c = 2
#
# Example Output:
# 6
#
# Explanation:
# In row 4 → elements are [1, 4, 6, 4, 1]
# Index 2 → value is 6


###################
# Better Approach #
###################

# - Create a function to calculate factorial
# - Use nCr formula to find the value
#
# - Call factorial(row)
# - Call factorial(column)
# - Call factorial(row - column)
#
# - Then apply:
#   nCr = row! / (column! * (row - column)!)

def factorial(n):
    if n == 0 or n == 1:
        return 1
    
    fact = 1
    for i in range(n,0,-1):
        fact = fact * i
    
    return fact

def pascalElementWithFactorial(r,c):
    nCr = factorial(r) // (factorial(c) * factorial(r-c))
    return nCr

print(pascalElementWithFactorial(4,2))

####################
# Optimal Approach #
####################

def pascalElementFind(r,c):
    if c > r:
        return 0
    res = 1
    c = min(c, r - c)

    for i in range(c):
        res = res * (r-i)
        res = res // (i+1)
    
    return res

print(pascalElementFind(4,2))

# TC = O(min(c, r - c))