# remove duplicates element inside sorted array

def removeDuplicatesElements(arr):
    if not arr or len(arr) < 2:
        return;

    newArr = [arr[0]]

    for i in range(1,len(arr) ):
        if arr[i - 1] < arr[i]:
            newArr.append(arr[i])
    return newArr


arr = [1,1,2,2,3,4,4,5,5,6] # [1,2,3,4,5]

print(f"After remove duplicate new array look like {removeDuplicatesElements(arr)}")

# above question we return arr and here we create new array so space complexity may be to up.
# to solve we use two pointers 
# and function return only index values and function modify argument send array.

def newRemoveDuplicatesElements(arr):
    if not arr:
        return 0;

    i = 0
    for j in range(1, len(arr)):
        if arr[j] > arr[i]:
            i += 1
            arr[i] = arr[j]

    return i + 1


arr = [1,1,2,2,3,3,4,4,5,5,6]

length = newRemoveDuplicatesElements(arr)

print(f"new array after duplicates element remove is {arr[:length]}")

# for both TC O(n)
# but better SC.