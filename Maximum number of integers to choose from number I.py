class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        # Convert the list of banned numbers to a set for faster lookups
        banned_set = set(banned) # Use a set for the quick lookups

        # Initialize variables:
        # total_sum to keep track of the sum of selected numbers 
        # count to keep track of the number of valid integers included


        total_sum = 0 # Track the cumulative sum 
        count = 0 # Track the count of valid numbers

        # Iterate through numbers from 1 to n

        # Skip the current number if it is in the banned set
        for i in range(1, n+1):
            if i in banned_set:
                continue # Skip banned numbers

            # Add the current number to the total sum
            total_sum += i 

            # If the total sum exeeds maxSum, stop processing further
            if total_sum > maxSum:
                break # Stop if the sum exeeds the maxsum 
            # Increment the count of the valid numbers included
            count += 1
        # Return the total count of numbers that can be included without exceeding maxSum
        return count
        
