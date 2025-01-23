class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
        # Get the dimensions of the grid (rows and columns)
        m, n = len(grid), len(grid[0])

        # Initialize arrays to count the number of servers in each row and column
        row = [0] * n # Counts servers in each columnn
        col = [0] * m # Counts servers in each row

        # First pass: Count the number of servers in each row and column
        for i in range(m):
            for j in range(n):
                if grid[i][j]  == 1: # If there's a server at (i,j)
                    row[j] += 1 # Increment the count for column j
                    col[i] += 1 # Increment the count for row i 
        ans = 0 

        # Second pass: Check if a server can communicate with at least one other server
        for i in range(m):
            for j in range(n):
                # A server can communicate if:
                # - It's at (i,j)(grid[i][j] == 1), and 
                # - The sum of servers in its row and column is greater than 2
                # Subtracting 1 for the current server itself
                if grid[i][j] == 1 and (row[j] + col[i]) > 2:
                    ans += 1 # Increment the count of communicable servers
        # Return the total number of communicable server
        return ans
        
