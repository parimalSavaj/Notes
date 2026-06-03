def intersectionOfTwoSortedArray(arr1,arr2):
    n1, n2 = len(arr1), len(arr2)
    i, j = 0, 0
    intersectionArr = []

    while i < n1 and j < n2:
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            if not intersectionArr or intersectionArr[-1] != arr1[i]:
                intersectionArr.append(arr1[i])
            i += 1
            j += 1
            
    return intersectionArr

arr1 = [1, 1, 2]
arr2 = [1, 1, 1, 2]

print(intersectionOfTwoSortedArray(arr1, arr2))

# TC O(n + m)
# SC O(n)
