# left rotate array by D places. 

def leftRotateArrByDPlaces(arr,n):
    if not arr:
        return
    
    length = len(arr)
    
    temp = arr[:n]

    for i in range(n,length):
        arr[i-n] = arr[i]
    
    for i in range(length-n,length):
        arr[i] = temp[i - (length - n)] # The right part after the equal sign here is tricky.

    return arr

array = [1,2,3,4,5,6,7]
# print(f"after rotate 3 place new array look like {leftRotateArrByDPlaces(array,3)}")
print(f"after rotate 4 place new array look like {leftRotateArrByDPlaces(array,4)}")