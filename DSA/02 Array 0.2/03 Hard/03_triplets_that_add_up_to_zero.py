# 3 Sum Problem

# Find all unique triplets
# whose sum becomes 0.

# A triplet means:
# choosing 3 different elements
# from the array.

# Example:
# nums = [-1, 0, 1, 2, -1, -4]

# Valid triplets:
# [-1, 0, 1]
# [-1, -1, 2]

# Because:
# -1 + 0 + 1 = 0
# -1 + -1 + 2 = 0

# Output:
# [[-1, -1, 2], [-1, 0, 1]]

# Important:
# Do not store duplicate triplets.

# Main goal:
# Find all unique combinations
# of 3 numbers whose sum is 0.

####################
#     Better       #
####################

def find_triplet(nums):
    unique_triplet = set()

    for i in range(len(nums)):
        temp_set = set()

        for j in range(i+1, len(nums)):

            third_num = -(nums[i] + nums[j])

            if third_num in temp_set:
                current_triplet = sorted([nums[i],nums[j],third_num])
                unique_triplet.add(tuple(current_triplet))
            
            temp_set.add(nums[j])
    
    result = [list(item) for item in unique_triplet]

    return result

nums = [-1, 0, 1, 2, -1, -4]

print(find_triplet(nums))

# TC O(n ^ 2)
# SC O(n)


####################
#     Optimal      #
####################

def gives_triplets(nums):
    nums.sort()
    n = len(nums)
    result = []

    for i in range(n - 2):
        if i > 0 and nums[i] == nums[i-1]: continue

        j = i + 1
        k = n - 1

        while(j < k):
            current_sum = nums[i] + nums[j] + nums[k]

            if current_sum > 0:
                k -= 1
            elif current_sum < 0:
                j += 1
            else:
                result.append([nums[i], nums[j], nums[k]])
                j += 1
                k -= 1

                while( j < k and nums[j] == nums[j - 1]): j += 1
                while( j < k and nums[k] == nums[k + 1]): k -= 1

    return result

# TC O(n ^ 2)
# SC O(1)