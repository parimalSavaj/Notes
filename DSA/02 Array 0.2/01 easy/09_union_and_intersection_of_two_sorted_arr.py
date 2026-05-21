# find union and intersection of two sorted arrays.

def union(arr1, arr2):
    st = set()

    for i in arr1:
        st.add(i)

    for i in arr2:
        st.add(i)

    unionArr = []

    for i in st:
        unionArr.append(i)

    return unionArr;

arr1 = [1,2,4,5,6]
arr2 = [2,3,5,6,7]

print(f"union is {union(arr1, arr2)}")

# TC O(n)+O(m)+O(n+m) = O(n+m)
# SC O(n+m) 
# Space Complexity (Including Everything)
# Set (st) → stores up to n + m
# List (unionArr) → also up to n + m