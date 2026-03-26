# find union and intersection of two sorted arrays.
# two pointer method

def union(arr1, arr2):
    unionArr = []

    i = 0
    j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            if not unionArr or unionArr[-1] < arr1[i]:
                unionArr.append(arr1[i])
            i+=1
        else:
            if not unionArr or unionArr[-1] < arr2[j]:
                unionArr.append(arr2[j])
            j+=1
    
    while i < len(arr1):
        if not unionArr or unionArr[-1] < arr1[i]:
            unionArr.append(arr1[i])
        i+=1

    while j < len(arr2):
        if not unionArr or unionArr[-1] < arr2[j]:
            unionArr.append(arr2[j])
        j+=1

    return unionArr

arr1 = [1,2,4,5,6]
arr2 = [2,3,4,6,7]

print(f"union is {union(arr1, arr2)}")

# TC O(n+m)
# SC O(n+m)