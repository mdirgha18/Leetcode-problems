class Solution:
    def minOperations(self, grid: List[List[int]], x: int) -> int:
        # Step 1: Flatten the 2D grid into a 1D list 
        values = sorted([val for row in grid for val in row])

        # Step 2: Check if all the values can be transformed into a common number
        # Compute the remainder when subtracting the first value and then divding by x
        diff = [abs(val - values[0]) % x for val in values]

        # If any remainder is not 0, it means transformation is possible 
        if any(d != 0 for d in diff):
            return -1 # No possible transformation 

        # Step 3: Find the median value of the sorted array
        median = values[len(values) // 2] # Select the middle element 

        # Step 4: Compute the minimum operations needed to make all values equal to the median 
        # Each operation increases/decreases a value by x 
        operations = sum(abs(val - median) // x for val in values)

        return operations # Return the minimum number of operations
        
