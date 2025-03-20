class Solution:
    def minimumCost(self, n: int, edges: List[List[int]], query: List[List[int]]) -> List[int]:
        # Initialize the parent array for the union-find
        parent = list(range(n))

        # Array to store the minimum path cost for each connected component
        min_path_cost = [-1] * n 

        # Function to find the root of the node (with path compression)
        def find_root(node: int) -> int:
            if parent[node] != node:
                parent[node] = find_root(parent[node]) # Path compression for optimization
            return parent[node]

        # Process each edge to build the union-find structure 
        for source, target, weight in edges:
            # Find the root of both the nodes 
            source_root = find_root(source)
            target_root = find_root(target)

            # Update the minimum path cost using bitwise AND operation
            min_path_cost[target_root] &= weight # Maintain the min cost component

            # If both the nodes belong to the different components, merge them
            if source_root != target_root:
                # Merge by applying bitwise AND to maintain minimum weight
                min_path_cost[target_root] &= min_path_cost[source_root]
                parent[source_root] = target_root # Update the parent to merge the components 

        result = []

        # Answer each query
        for start, end in query: 
            if start == end:
                result.append(0) # If both the nodes are same, cost is 0
            elif find_root(start) != find_root(end):
                result.append(-1) # If nodes are in different components, return -1
            else:
                result.append(min_path_cost[find_root(start)]) # Return min path cost in the component
        
        return result
        
