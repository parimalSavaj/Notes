# to move zeros to end of array
# using two pointer method

def moveZeroToEnd(arr):
    j = -1
    for i in range(0,len(arr)):
        if arr[i] == 0:
            j = i
            break
            
    for i in range(j+1,len(arr)):
        if arr[i] != 0:
            arr[i],arr[j] = arr[j],arr[i]
            j+=1

    return arr

arr = [0,1,2,0,3,4,0,5,0]

print(f"all zeros move to end and new array look like {moveZeroToEnd(arr)}")

# TC O(n)
# SC O(1)