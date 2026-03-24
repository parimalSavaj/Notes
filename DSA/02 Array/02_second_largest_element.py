# find second largest element in array

def secondLargestElement(arr):
    if not arr:
        return;

    firstLargestElement = arr[0]
    secondLargestElement = 0
    for i in arr:
        if firstLargestElement < i: # number is bigger then largest element
            secondLargestElement = firstLargestElement
            firstLargestElement = i
            continue
        if secondLargestElement < i and firstLargestElement > i: # number is bigger then second largest but smaller then largest
            secondLargestElement = i
    return secondLargestElement

arr = [1,7,7,7,7,7,7,7,7] # 1
# arr = [7,7,7,7,7,7,7,7,1] # 1
# arr = [7,1,5,7,6,2,4] # 6
# arr = [7,1,5,6,2,4] # 6
print(f"Second largest element is {secondLargestElement(arr)}")


# Time complexity O(n)
