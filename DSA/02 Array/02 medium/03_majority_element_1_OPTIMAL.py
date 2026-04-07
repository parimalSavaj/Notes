def majorityElement(arr):
    element = None
    count= 0

    for i in arr:
        if count == 0:
            element = i
            
        count += 1 if i == element else -1    

    newCount = 0
    for i in arr:
        if i == element:
            newCount+=1
    
    if newCount > len(arr)//2:
        return element

arr = [2, 3, 2, 2, 3]

print(majorityElement(arr))

# TC O(2n)
# SC O(1)