# Problem: Stock Buy and Sell
#
# You are given an array of stock prices.
# Each element represents the price on that day.
#
# Task:
# Find the maximum profit by buying once and selling once.
#
# Notes:
# - You must buy before you sell
# - Only one transaction allowed
# - If no profit is possible, return 0
#
# Example:
# Input: [7, 1, 5, 3, 6, 4]
# Output: 5
# Explanation: Buy at 1 and sell at 6 → profit = 5

def maxProfit(arr):
    profit,minimum = 0,arr[0]

    for i in range(1,len(arr)):
        cost = arr[i] - minimum 
        profit = max(cost,profit)
        minimum = min(minimum,arr[i])

    return profit

arr = [7, 1, 5, 3, 6, 4]

print(maxProfit(arr))

# TC O(n)
# SC O(1)