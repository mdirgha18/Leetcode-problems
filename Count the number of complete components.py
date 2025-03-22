from collections import defaultdict

class Solution(object):
    def countCompleteComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        # Step 1: Build an adjacency list representation of the graph 
        graph = defaultdict(list)

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        # Step 2: Initialize a visited set to track visited nodes 
        visited = set()
        count = 0 # Count of complete components 

        def dfs(node, component):
            # Perform DFS to find all the nodes in the same connected component
            component.add(node)
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor, component)
        # Step 3: Iterate through all the nodes to find the connected components 
        for i in range(n):
            if i not in visited:
                component = set()
                dfs(i, component) # Find all the nodes in the current component


                # Step 4: Check if the component is complete 
                # A component is complete if every node has exactly (size - 1) edges
                if all(len(graph[node]) == len(component) - 1 for node in component):
                    count += 1 # Increment count if the component is complete

        return count # Return the total number of complete components
        
