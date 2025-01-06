class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # Length of the input string
        n = len(boxes)
        # Initialize the result array to store the minimum operations for each box
        res = [0] * n 

        # Variables for left-to-right traversal
        val = 0 # Cumulative operations count
        count = 0 # Number of balls encountered so far

        # Traverse the string from left to right
        for i in range(n):
            # Add the cumulative operations to the current box
            res[i] += val 
            # If the current box contains a ball ('l'), increase the count of balls
            if boxes[i] == '1':
                count += 1
            # Add the number of balls encountered so far to the cumulative operations
            val += count 

        # Reset variables for right-to-left traversal 

        val = 0 
        count = 0

        # Traverse the string from right to left
        for i in range(n - 1, -1, -1):
            # Add the cumulative operations to the current box
            res[i] += val 
            # If the current box contains a ball ('l'), increase the count of balls
            if boxes[i] == '1':
                count += 1
            # Add the number of balls encountered so far to the cumulative operations
            val += count

        # Return the final result array containing the minimum operations for each box
        return res

        
