class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:

        # Calculates the height of each cell in a grid such that 
        # water cells have height 0 
        # Heights increase by 1 as we move further away from water cells 

        # Args: isWater(List[List[int]]): A 2D grid where 1 represents water and 0 represents land 
        # Returns: List[List[int]]: A 2D grid with the calculated heights

        # Get the dimensions of the grid (rows: m, columns: n)
        m,n = len(isWater), len(isWater[0])

        # Initialize the heights grid with -1 to indicate celss
        heights = [[-1] * n for _ in range(m)]
        queue = deque()

        # Define the 4 possible directions to move (right, down, left, up)
        directions = [(0,1),(1,0),(0,-1),(-1,0)]

        # Add all water cells to the queue and set their height to 0 
        for i in range(m):
            for j in range(n):
                if isWater[i][j] == 1:
                    heights[i][j] = 0 # Water cells have height 0
                    queue.append((i,j)) # Enqueue the coordinates of the water cell

        # Perform BFS to calculate heights for all the cells 
        while queue:
            # Dequeue the next cell to process
            x,y = queue.popleft()

            # Check all 4 neighbouring cells 
            for dx, dy in directions:
                nx, ny = x + dx, y + dy # Calculate new coordinates 

                # If the neighbor is within bounds and unvisited
                if 0 <= nx < m and 0 <= ny < n and heights[nx][ny] == -1:
                    # Set the height of the neighbor to be 1 more than the current cell
                    heights[nx][ny] = heights[x][y] + 1

                    # Enqueue the neighbor for the further processing
                    queue.append((nx, ny))
        # Return the grid with the calculated heights 
        return heights        
