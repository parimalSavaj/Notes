# Problem: Union of Two Sorted Arrays
#
# Given two sorted arrays, find the union of both arrays.
#
# The resulting collection should contain every unique element from both
# arrays while maintaining sorted order.
#
# Example:
# Array 1: [1, 2, 3, 4, 5]
# Array 2: [1, 2, 3, 6, 7]
#
# Output:
# [1, 2, 3, 4, 5, 6, 7]

def unionOfTwoSortedArr(arr1, arr2):
    n1, n2 = len(arr1), len(arr2)
    i, j = 0, 0
    unionArr = []

    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            if not unionArr or unionArr[-1] != arr1[i]:
                unionArr.append(arr1[i])
            i += 1

        elif arr1[i] > arr2[j]:
            if not unionArr or unionArr[-1] != arr2[j]:
                unionArr.append(arr2[j])
            j += 1

        else:
            if not unionArr or unionArr[-1] != arr1[i]:
                unionArr.append(arr1[i])
            i += 1
            j += 1

    while i < n1:
        if not unionArr or unionArr[-1] != arr1[i]:
            unionArr.append(arr1[i])
        i += 1

    while j < n2:
        if not unionArr or unionArr[-1] != arr2[j]:
            unionArr.append(arr2[j])
        j += 1

    return unionArr


arr1 = [1, 2, 2, 3]
arr2 = [2, 2, 4]
print(unionOfTwoSortedArr(arr1,arr2))

# TC O(n + m)
# SC O(n + m)