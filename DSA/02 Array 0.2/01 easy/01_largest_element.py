# first largest element in array

def largestElement(arr):

    if not arr:
        return;

    largest = arr[0]
    for i in arr:
        if largest < i:
            largest = i
    
    return largest;


arr = []
print(f"Largest Element is {largestElement(arr)}")

# Time complexity is O(n)