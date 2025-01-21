class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:

        # Determine the minimum score that Robot 2 can achieve when Robot 1 moves optimally 
        # List[List[int]]) contains a 2 X N grid where each cell contains a positive integer score
        # It returns int - the minimum score the robot can achieve

        # Initialize the minimum result with infinity, as we are looking for the minimum possible value
        min_result = float('inf')

        # Calculate the initial sum of the first row (Robot 1's potential initial total)
        row1_sum = sum(grid[0])

        # Initialize the sum for the second row (Robot 2 starts with 0 points)
        row2_sum = 0 

        # Iterate through each column of the grid


        for i in range(len(grid[0])):
            # Robot 1 moves right, so subtract the current cell from Robot's 1's remaining sum
            row1_sum -= grid[0][i]

            # Calculate the maximum score Robot 2 can be forced to take 
            # Robot 1 chooses a strategy to minimize Robot 2's score
            min_result = min(min_result, max(row1_sum, row2_sum))

            # Add the current cell to Robot 2's cumulative score as Robot 2 moves up 
            row2_sum += grid[1][i]


        # Return the minimum result calculated
        return min_result

        
