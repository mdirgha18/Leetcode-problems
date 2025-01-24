class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        # Get the total number of nodes in the graph
        n = len(graph)

        # Initialize a list to store the eventual safe nodes
        res = []

        # A set to track nodes currently being visited in a DFS traversal (used to detect cycles)
        visited = set()

        # Memoization array:
        # memo[i] = 1: node'i' is eventually safe
        # memo[i] = -1: node 'i' is a part of a cycle or leads to a cycle 
        # memo[i] = 0: node 'i' has not been process yet
        memo = [0] * n 

        # Helper function to perform DFS on node 'i'
        def dfs(i):
            # If node 'i' is already marked as safe, return True 
            if memo[i] == 1 or len(graph[i]) == 0:
                return True 
            # If node 'i' is already marked as unsafe or is in current 'visited' set (cycle detected), return False
            elif memo[i] == -1 or i in visited:
                return False 
            
            # Mark the node as visited
            visited.add(i)

            # Perform DFS for all neighbors of node 'i'
            for neighbour in graph[i]:
                # If any neighbor leads to a cycle, mark node 'i' as unsafe
                if not dfs(neighbour):
                    memo[i] = -1 # Mark node 'i' as unsafe
                    return False 

            # If all neighbors are safe, mark node 'i' as safe
            memo[i] = 1
            return True

        # Iterate through all nodes in the graph
        for i in range(n):
            # Perform DFS for each node; if it is eventually safe, add it to the result
            if dfs(i):
                res.append(i)
        
        # Return the result of the eventual safe nodes in ascending order
        return res

        
