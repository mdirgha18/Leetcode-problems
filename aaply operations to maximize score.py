from typing import List

class Solution:
    MOD = 1000000007 # Large prime number for modulo operations

    def  maximumScore(self, nums:List[int], k: int) -> int:
        n = len(nums)
        upper = max(nums) + 1 # Find the max numbers in nums and define upper limit 

        # Compute prime factor counts (primeScore)
        primeScore = [0] * upper 
        for i in range(2, upper):
            if primeScore[i] == 0: # i is prime
                for j in range(i, upper, i): # Mark the multiples of i 
                    primeScore[j] += 1 # Increase the count of distinct prime factors 

        # Monotonic stack for next greater element
        # Step 1: Compute prime factor counts (primeScore)
        nextGreaterElement = [n] * n # Default to n (out of bounds)
        prevGreaterOrEqualElement = [-1] * n # Default to -1 (out of bounds)
        stack = []

        # Compute prevGreaterOrEqualElement using a monotonic stack 
        for i in range(n):
            while stack and primeScore[nums[i]] > primeScore[nums[stack[-1]]]:
                stack.pop() # Remove elements with a lower primeScore
            prevGreaterOrEqualElement[i] = stack[-1] if stack else -1 # Store previous index
            stack.append(i) # Push current index into the stack

        stack.clear() # Clear the stack for the next computation

        # Compute nextGreaterElement using a monotonic stack (from right to left)
        for i in range(n - 1, -1, -1):
            while stack and primeScore[nums[i]] >= primeScore[nums[stack[-1]]]:
                stack.pop() # Remove element with a lower or equal primeScore
            nextGreaterElement[i] = stack[-1] if stack else n # Store next greater index
            stack.append(i) # Push current index onto the stack

        # Sort indices based on values in descending order
        # Step 3: Sort indices based on nums[i] in descending order
        sorted_indices = sorted(range(n), key=lambda i: nums[i], reverse=True)

        # Step 4: Compute the result using the sorted indices
        res = 1 # Initialize result
        for idx in sorted_indices:
            num = nums[idx] # Current number
            operations = min((idx - prevGreaterOrEqualElement[idx]) * (nextGreaterElement[idx] - idx), k)
            res = (res * pow(num, operations, self.MOD)) % self.MOD # Comput power with the modulo
            k -= operations # Reduce remaining operations 
            if k == 0: # If all k operations are used up, return result
                return res
        
        return res # Return result if loop completes 
