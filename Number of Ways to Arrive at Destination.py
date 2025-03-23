class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) -> int:
        # Step1: Construct the adjacency list representation of the graph
        graph = [[] for _ in range(n)]
        for u,v, time in roads:
            graph[u].append((v,time)) # Bidirectional edge 
            graph[v].append((u,time))

        # Step 2: Initialize distance and ways arrays
        dist = [float('inf')] * n # Stores the shortest distance to each node 
        ways = [0] * n # Stores the number of shortest paths to each node 


        # Step 3: Start from node 0 
        dist[0] = 0 # Distance to the source node is 0 
        ways[0] = 1 # There is only 1 way to be at the start node

        
        # Priority queue for the Dijkstra's algorithm
        pq = [(0,0)] # (distance, node)


        MOD = 10**9 + 7 # To keep the results within the limits 

        # Dijkstra's algorithm
        while pq:
            d, node = heapq.heappop(pq) # Get the node with the strongest known distance

            if d > dist[node]:
                # If we encounter an outdated distance value, skip processing
                continue

            # Step 5: Explore neighbors
            for neighbor, time in graph[node]:
                if dist[node] + time < dist[neighbor]:
                    # If we found a shorter path to the neighbor
                    dist[neighbor] = dist[node] + time # Update the shortest distance 
                    ways[neighbor] = ways[node] # Reset path count to this newest shortest path
                    heapq.heappush(pq, (dist[neighbor], neighbor)) # Push updated distance to the heap 
                elif dist[node] + time == dist[neighbor]:
                    # If we found the another shortest path to the neighbor 
                    ways[neighbor] = (ways[neighbor] + ways[node]) % MOD # Accumulate ways 

        # Step 6: Return the number of shortest paths to node n - 1
        return ways[n-1]

        
