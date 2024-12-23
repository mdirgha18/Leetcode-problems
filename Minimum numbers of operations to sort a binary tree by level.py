# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minSwapsToSort(self, arr):
        # This function calculates the minimum number of swaps needed to sort an array 
        # It uses the concept of cycle detection in a graph where eahc element points to its 
        # sorted position 
        n = len(arr)
        # Pair each element with its index and sort by element value
        indexedArr = [(arr[i], i) for i in range(n)]
        indexedArr.sort()
        visited = [False] * n # To keep track of the visited indices 
        swaps = 0 # Count of swaps needed

        for i in range(n):
            # If element is already visited or in its correct position, skip 
            if visited[i] or indexedArr[i][1] == i:
                continue

            # Count the size of the cycle 
            cycleSize = 0   
            j = i
            while not visited[j]:
                visited[j] = True
                j = indexedArr[j][1] # Move to the index of the current element in the sorted order
                cycleSize += 1
            
            # If there's a cycle of size > 1, it requires (cycleSize - 1) swaps 
            if cycleSize > 1: 
                swaps += cycleSize - 1 
        return swaps

    def minimumOperations(self, root: Optional[TreeNode]) -> int:
        # This function calculates the minimum number of operations required 
        # to make each level of a binary tree sorted in the non-decreasing order. 
        # It uses BFS to traverse the tree level by level
        if not root:
            return 0  # If the tree is empty, no operations are needed

        queue = [root] # Start with the root node in the queue
        operations = 0 # To store the total number of operations 

        while queue:
            levelSize = len(queue) # NUmber of nodes at the current level
            level = [] # To store the values of nodes at this level 

            # Traverse all nodes in the current level 
            for _ in range(levelSize):
                node = queue.pop(0) # Dequeue the front node
                level.append(node.val) # Add its value to the level array

                # Add child nodes to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            # Calculate the minimum swaps needed to sort this level
            operations += self.minSwapsToSort(level)

        return operations


            



        
