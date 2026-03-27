# find missing number in an array.

# An array (list) of numbers
# The numbers are usually in a specific range (like 1 to N)
# But one number is missing

# Your job: figure out which number is missing an array.

# optimal No: 1

def missingNumUsingSumMethod(arr,N):
    sumOfN = (N * (N+1)) / 2

    sum = 0
    for i in arr:
        sum+=i
    
    missingNumber = sumOfN - sum
    return missingNumber

arr = [1,2,3,5,6]
print(f"Missing number is {int(missingNumUsingSumMethod(arr,6))}")

# TC O(n)
# SC O(1) 
#! this is good but what if arr length is 10 power 10 so sumOfN variable not handle this big value

# optimal No: 2

def findMissingNumUsingXOR(arr,N):
    xor1 = 0
    xor2 = 0 ^ N

    for i in range(0,len(arr)):
        xor1= xor1 ^ arr[i]
        xor2 = xor2 ^ (i+1)
    
    missNum = xor2 ^ xor1

    return missNum

arr = [1,2,3,5,6]
print(f"Using XOR method missing number is {findMissingNumUsingXOR(arr,6)}")

# TC O(N)
# SC O(1)