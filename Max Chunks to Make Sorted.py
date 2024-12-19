class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        # Initialize `cnt` to count the number of chunks we can form
        # Initialize `diff` to keep track of the difference between the cumulative sums of the elements in `arr` and their indices 
        cnt = diff = 0 
        # Iterate through the array using both index `i` and value `x`
        for i, x in enumerate(arr):
            # Update `diff` with the difference between the value at the current position and its index 
            diff += x-i
            # If `diff` becomes 0, it means all elements up to this index can form a sorted chunk
            cnt+=(diff==0)
        # Return the total number of chunks that can be formed
        return cnt
        
