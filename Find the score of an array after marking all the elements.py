class Solution:
    def findScore(self, nums: List[int]) -> int:
        # Create a min-heap of tuples where each tuple is (value, index)
        heap = [(n,i) for i,n in enumerate(nums)]

        # Create a set to track the indices that have been "marked" (either directly or adjacent)
        marked = set()

        # Convert the list 'heap' into a valid heap (in-place operation)
        heapify(heap)

        # Initialize the result variable that will hold the score
        res = 0 

        # WHile thehre are still elements in the heap
        while heap: 
            # Pop the smallest element (value, index) from the heap
            n, i = heappop(heap)

            # If the index 'i' has already been marked, skip this element
            if i in marked:
                continue

            # Mark the current index 'i' and its adjacent indices (i-1, i+1)
            marked.add(i - 1)
            marked.add(i + 1)

            # Add the value 'n' of the current element to the result
            res += n 
            
        # Return the final score (sum of select elements' values)
        return res
