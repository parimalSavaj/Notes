# Given an array of size N,
# find all elements that appear
# more than N/3 times.

# An element is called a majority element
# if its frequency is greater than N/3.

# Return all such elements present in the array.

# Example:
# nums = [1,2,1,1,3,2,2]

# N = 7
# N/3 = 2

# Elements appearing more than 2 times:
# 1 -> 3 times
# 2 -> 3 times

# Output: [1, 2]

####################
#     Better       #
####################

def majorityElement(arr):

    n = len(arr)

    freq = {}
    ans = []

    for num in arr:
        freq[num] = freq.get(num, 0) + 1

    for key, value in freq.items():

        if value > n // 3:
            ans.append(key)

    return ans

####################
#     Optimal      #
####################

def majorityElement(arr):
    n = len(arr)
    count1, count2 = 0, 0
    num1, num2 = 0, 0

    for i in range(0,n):
        if count1 == 0 and num2 != arr[i]:
            count1 = 1
            num1 = arr[i]
        elif count2 == 0 and num1 != arr[i]:
            count2 = 1
            num2 = arr[i]
        elif arr[i] == num1:
            count1 += 1
        elif arr[i] == num2:
            count2 += 1
        else:
            count1 -= 1
            count2 -= 1
    
    count1, count2 = 0, 0

    for i in range(0,n):
        if num1 == arr[i]:
            count1 += 1
        if num2 == arr[i]:
            count2 += 1
    
    list = []

    if count1 > n // 3:
        list.append(num1)
    if count2 > n // 3:
        list.append(num2)
    
    return list

print(majorityElement([1, 2, 1, 1, 3, 2]))

# TC O(2n)
# SC O(1)