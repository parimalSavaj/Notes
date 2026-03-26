# find intersection of two sorted arrays.
# two pointer method

def union(arr1, arr2):
    intersectionArr = []

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr1[i]:
            j += 1
        else:
            if not intersectionArr or intersectionArr[-1] != arr1[i]: 
                # most impotent condition to avoid result like
                # arr1 = [1, 2, 2, 2, 3]
                # arr2 = [2, 2, 3] 
                # interArr = [2, 2, 2, 3]   ❌ duplicates
                intersectionArr.append(arr1[i]) 
            i += 1
            j += 1

    return intersectionArr

arr1 = [1,2,4,4,4,4,4,5,6]
arr2 = [2,3,4,6,7]

print(f"union is {union(arr1, arr2)}")

# TC O(n+m)
# SC O(n+m)