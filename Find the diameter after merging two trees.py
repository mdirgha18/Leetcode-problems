from collections import defaultdict, deque
import heapq

class Solution:
    def minimumDiameterAfterMerge(self, edges1, edges2):
        # Step 1: Build adjacency list for both trees 
        # Convert the list of edges into adjacency lists for efficient graph traversal
        adjList1 = self.buildAdjList(edges1)
        adjList2 = self.buildAdjList(edges2)
        
        # Step 2: Perform topoloogical sorting (actually it's the twp farthest nodes approach)
        # This is effectively finding the two farthest nodes in each tree
        diameter1 = self.topologicalSort(adjList1)
        diameter2 = self.topologicalSort(adjList2)

        # Step 3: Extract the longest and second longest distances from the two trees

        secondLongest1 = 0 
        longest1 = 0 
        secondLongest2 = 0 
        longest2 = 0 

        # Retrieve the two largest distances for the first tree
        if len(diameter1) == 2:
            secondLongest1 = heapq.heappop(diameter1)
            longest1 = heapq.heappop(diameter1)
        else:
            longest1 = heapq.heappop(diameter1)

        # Retrieve the two largest distances for the second tree
        if len(diameter2) == 2:
            secondLongest2 = heapq.heappop(diameter2) 
            longest2 = heapq.heappop(diameter2)
        else: 
            longest2 = heapq.heappop(diameter2)

        # Step 4: Return the maximum possible diameter after merging
        # The maximum diameter is determined by combining the largest distances from the both trees
        return max(secondLongest1 + longest1, max(secondLongest2 + longest2, longest1 + longest2 + 1))

    def topologicalSort(self, adjList):
        # This function returns the two largest distances using a topological traversal like BFS/DFS
        # This function calculates the two largest distances using a BFS-like traversal
        # It simulates topological sorting for unrooted trees to find the farthest nodes

        # Count the degree of each node (number of connected edges)
        indegree = {key: len(adjList[key]) for key in adjList}
        queue = deque()
        res = []

        # Initialize queue with nodes having only one edge 
        # Initialize queue with leaf nodes (nodes having only one edge)
        for key in adjList:
            if indegree[key] == 1:
                queue.append((key, 0))

        # Perform BFS to calculate distances
        while queue:
            node, dist = queue.popleft()

            for adj in adjList[node]:
                if indegree[adj] > 0:
                    # Decrement the degree of the adjacent node
                    if indegree[adj] > 1:
                        indegree[adj] -= 1
                    if indegree[adj] == 1:
                        # Add the adjacenet node to queue with updated distance
                        queue.append((adj, dist + 1))
                        heapq.heappush(res, dist + 1)
                        # Maintain only the top 2 distances in the heap
                        if len(res) > 2:
                            heapq.heappop(res)
            # Decrement the degree of the current node
            indegree[node] -= 1
            if not queue:
                break
        # If no distances were calculated, add a default value
        if not res:
            res.append(0)
        return res

    def buildAdjList(self, edges):
        # This function builds he adjacency list from the edges list
        adjList = defaultdict(list)

        for u,v in edges:
            adjList[u].append(v)
            adjList[v].append(u)
        return adjList




        
