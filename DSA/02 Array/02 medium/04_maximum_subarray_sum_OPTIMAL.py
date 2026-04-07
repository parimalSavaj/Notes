def subArray(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        if current_sum + arr[i] > arr[i]:
            current_sum = current_sum + arr[i]
        else:
            current_sum = arr[i] # this case of all element are in negative

        if current_sum > max_sum: 
            max_sum = current_sum

    return max_sum


arr = [-2, -3, 4, -1, -2, 1, 5, -3]

print(f"output = {subArray(arr)}")

# TC O(n)
# SC O(1)