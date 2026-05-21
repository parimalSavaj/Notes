def longestConsecutiveArr(arr):
    arrDic = dict.fromkeys(arr)
    longest = 0
    
    for i in arr:
        if i-1 in arrDic:
            continue
        count = 1
        current = i

        while current + 1 in arrDic:
            count += 1
            current += 1
        
        longest = max(longest,count)

    return longest

arr = [100, 4, 200, 1, 3, 2]

print(longestConsecutiveArr(arr))

# TC O(3n)
# SC O(n)
