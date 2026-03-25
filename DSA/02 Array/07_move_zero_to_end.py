# to move zeros to end of array  

def moveZeroToEnd(arr):
    temp = []
    for i in range(0,len(arr)):
        if arr[i] != 0:
            temp.append(arr[i])
    
    for i in range(0,len(temp)):
        arr[i] = temp[i]

    for i in range(len(temp),len(arr)):
        arr[i] = 0
    
    return arr

arr = [0,1,2,0,3,4,0,5,0]

print(f"all zeros move to end and new array look like {moveZeroToEnd(arr)}")

# TC O(2n)
# SC O(n)