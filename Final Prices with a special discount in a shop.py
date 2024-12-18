class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # Get the length of the prices list
        n = len(prices)

        # Initialize a stack to store indices, starting with the last index
        stack = [n-1]

        # Create a copy of the prices to store the final results 
        ans = [x for x in prices]

        # Iterate through prices list from the second-to-last element to the first
        for i in range(n-2, -1, -1):
            # Remove indices from the stack where the corresponding price is greater than 'prices[i]'
            while stack and prices[i] < prices[stack[-1]]:
                stack.pop()
            # If the stack is not empty, subtract the next smaller price from the current price
            if stack: ans[i] -= prices[stack[-1]]

            # Add the current index to the stack
            stack.append(i)
        # Return the final list of the discounted prices 
        return ans
        
