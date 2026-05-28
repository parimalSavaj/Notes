def secondLargestNum(arr):
    if not arr or len(arr) < 2:
        return None
    
    largest = arr[0]
    secondLargest = float('-inf')

    for num in arr:
        if num > largest:
            secondLargest = largest
            largest = num
        elif num < largest and num > secondLargest:
            secondLargest = num

    if secondLargest == float('-inf'):
        return None

    return secondLargest

arr = [3, 7, 2, 9, 5]

print(secondLargestNum(arr))

# TC O(N)
# SC O(1)

#####################################
#   second smallest
#####################################

def secondSmallestNum(arr):
    if not arr or len(arr) < 2:
        return None
    
    smallest = float('inf')
    secondSmallest = float('inf')

    for num in arr:
        if num < smallest:
            secondSmallest = smallest
            smallest = num

        elif num > smallest and num < secondSmallest:
            secondSmallest = num

    if secondSmallest == float('inf'):
        return None

    return secondSmallest

# TC O(n)
# SC O(1)