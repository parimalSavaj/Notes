def rotateMatrix(matrix):
    n = len(matrix)
    

    for i in range(0,n-1): # for i range(n):
        for j in range(i+1, n):  # for j in range(i,n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
    
    for i in range(n):
        matrix[i].reverse()
    
    return matrix

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

result = rotateMatrix(matrix)

print(result)