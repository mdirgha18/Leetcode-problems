class Solution:
    def maxPoints(self, grid: list[list[int]], queries: list[int]) -> list[int]:
        # Get dimensions of the grid 
        rows, cols = len(grid), len(grid[0])
        q_len = len(queries)

        # Sort queries along with their original indices
        queries_idx = sorted((val, i) for i, val in enumerate(queries))

        # min-heap to explore grid cells (sorted by values)
        min_heap = [(grid[0][0], 0, 0)] # value, row, col
        visited = set()
        visited.add((0, 0)) # track visited cells 

        # Results to store the answers for each query
        result = [0] * q_len
        count = 0 # tracks the number of cells visited

        # Possible movement directions: right, down, left, up
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        # Process each query in sorted order
        for query, i in queries_idx:

            # Expand min-heap untill the top element is >= query value
            while min_heap and min_heap[0][0] < query:
                value, r, c = heappop(min_heap) # Get the smallest cell value
                count += 1 # Increase count of the reachable cells 

                # Explore all 4 possible directions 
                for dr, dc in directions: 
                    nr, nc = r + dr, c + dc 

                    # Check boundaries and if not visited
                    if 0 <= nr < rows and 0 <= nc < cols and (nr, nc) not in visited:
                        heappush(min_heap, (grid[nr][nc], nr, nc)) # Push new cell into a heap
                        visited.add((nr, nc)) # Mark as visited

            # Store the count of visited cells for this query
            result[i] = count
        
        return result
