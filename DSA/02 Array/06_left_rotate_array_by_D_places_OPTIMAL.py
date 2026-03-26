# optimal way for left rotate array by D places.

def leftRotate(arr,d):
    length = len(arr)

    def reverse(start,end):
        while start < end:
            arr[start],arr[end]=arr[end],arr[start]
            start+=1
            end-=1

    reverse(0,d - 1)
    reverse(d,length-1)
    reverse(0,length-1)

    return arr

arr = [1,2,3,4,5,6,7]

# print(f"after rotate {3} places new array look like {leftRotate(arr,3)}")
print(f"after rotate {4} places new array look like {leftRotate(arr,4)}")
# print(f"after rotate {8} places new array look like {leftRotate(arr,8)}")

