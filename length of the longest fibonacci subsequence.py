from typing import List

class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        n = len(arr) # Get the length of the array 
        dp = [[0] * n for _ in range(n)] # Initialize the 2D list to store the lengths of the Fibonacci sequences
        maxLen = 0 # Variable to track the maximum length of the fibonacci subsequence

        # Iterate over  each element of the array starting from the third element (index 2)
        for curr in range(2, n): 
            start, end = 0, curr - 1 # Set the starting and ending pointers to the first two elements before curr
            
            # While the start pointer is less than the end pointer 
            while start < end:
                pairSum = arr[start] + arr[end] # Calculate the sum of two numbers at 'start' and 'end'
                if pairSum > arr[curr]: # If the sum is greater than the current element, 'move' the end pointer to the left
                    end -= 1
                elif pairSum < arr[curr]: # If the sum is smaller, 'move' the start pointer to the right
                    start += 1 
                else: # If the sum matches the current element, we've found a valid Fibonacci sequence
                    dp[end][curr] = dp[start][end] + 1 # Update the dp table with the length of this subsequence
                    maxLen = max(dp[end][curr], maxLen) # Update the maximum length of any fibonacci sequence found
                    end -= 1 # Move the 'end' pointer to the left
                    start += 1 # Move the 'start' pointer to the right

        # If no valid sequence is found, return 0. Otherwise return the length of the longest fibonacci subsequence + 2
        return 0 if maxLen == 0 else maxLen + 2 

        
