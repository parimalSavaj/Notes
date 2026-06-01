# Left Rotate Array by K Places

# Idea:
# Move every element K positions to the left.
# Elements removed from the beginning are placed at the end.

# Example:
# arr = [1, 2, 3, 4, 5]
# k = 2

# First K elements:
# [1, 2]

# Remaining elements:
# [3, 4, 5]

# After left rotation:
# [3, 4, 5, 1, 2]

# Important:
# If k > n (array size),
# use k % n because rotating n times
# brings the array back to its original state.

# Example:
# n = 5, k = 7
# effective rotations = 7 % 5 = 2



#*####################################
#!            Better
#*####################################

def betterLeftRotate(arr,k):
    n = len(arr)
    k = k % n

    temp = []
    for i in range(0,k): # based on this loop we can write direct temp = [:k]
        temp.append(arr[i]) 

    for i in range(k,n):
        arr[i-k] = arr[i]

    for i in range(n-k,n):
        arr[i] = temp[i-(n-k)]

    return arr

arr = [1,2,3,4,5]
k = 4
# print(betterLeftRotate(arr,k))


# TC O(n)
# SC O(n)


#*####################################
#!            Optimal
#*####################################


def optimalLeftRotate(arr,k):
    def reversArr(array, left, right):
        while left < right:
            array[left], array[right] = array[right], array[left]
            left+=1
            right-=1
        

    n = len(arr)
    k = k % n

    reversArr(arr,0,k-1)
    reversArr(arr,k,n-1)
    reversArr(arr,0,n-1)

    return arr

arr = [1,2,3,4,5]
k = 4
print(optimalLeftRotate(arr,k))


# TC O(n)
# SC O(1)