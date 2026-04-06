def subArray(arr):
    max_sum = arr[0]
    current_sum = arr[0]

    for i in range(1, len(arr)):
        if current_sum + arr[i] > arr[i]:
            current_sum = current_sum + arr[i]
        else:
            current_sum = arr[i]

        if current_sum > max_sum:
            max_sum = current_sum

    return max_sum


arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

print(f"output = {subArray(arr)}")

# TC O(n)
# SC O(1)