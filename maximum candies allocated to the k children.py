class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Initialize the binary search range 
        left, right = 1, max(candies) # The minimum candy per child is 1 and the maximum can be the highest pile 
        result = 0 # Stores the maximum candies each child can recieve

        # Perform binary search
        while left <= right: 
            mid = (left + right) // 2 # Find the middle value as the possible max candies per child  

            # Calculate how many children can recieve 'mid' candies per child 
            children_count = sum(pile // mid for pile in candies) 

            # If we can distribute at least 'k' children, it is a valid distribution
            if children_count >= k:
                result = mid # Store the valid max count 
                left = mid + 1 # Try to find a valid larger value 
            else:
                right = mid - 1 # Reduce the search space

        return result # Return the maximum number of candies each child can get
