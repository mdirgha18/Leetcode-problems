class Solution:
    def punishmentNumber(self, n: int) -> int:
        # Precomputed list of numbers that satisfy the given condition 
        arr = [1,9,10,36,45,55,82,91,99,100,235,297,369,370,379,414,
               657,675,703,756,792,909,918,945,964,990,991,999,1000]

        total = 0 # Variable to store the sum of squared values
        # Iterate through the precomputedd list 
        for num in arr:
            if num <= n: # Check if the current number is within the given range
                total += num * num # Add its square to the total sum 
            else:
                break # Stop iterating once we exceed n
        return total # Return the final computed sum


        
