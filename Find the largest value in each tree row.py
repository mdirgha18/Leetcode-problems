from typing import Optional, List 


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val  # Value of the node
        self.left = left # Pointer to the left child 
        self.right = right # Pointer to the right child
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        # This function finds the largest value in each row of a binary tree
        # param root: The root of the binary tree 
        # rreturn - A list of the largest values for each level of the tree
        if not root: 
            # If the tree is empty, return an empty list
            return []

        result = [] # List to store the largest values for each level
        queue = deque([root]) # Initialize the queue with the root node

        # Perform level-order traversal of the tree
        while queue:
            level_size = len(queue) # Number of nodes at the current level
            max_val = float('-inf') # Initialize max_val to the smallest possible value

            # Iterate through all the nodes at the current level

            for _ in range(level_size):
                node = queue.popleft() # Remove the node from the front of the queue
                max_val = max(max_val, node.val) # update max_val with the node's value

                
            # Add the left child to the queue if it exists
                if node.left:
                    queue.append(node.left)
                # Add the right child to the queue if it exists
                if node.right:
                    queue.append(node.right)
            # After processing all nodes at the current level, append max_val to the result
            result.append(max_val)
        
        # Return the list of largest values for each level
        return result
        
