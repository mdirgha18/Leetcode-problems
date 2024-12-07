class Solution:
    def minimumSize(self, nums: List[int], maxOps: int) -> int:
        # Initialize the search range:
        # 'low' starts at 1 (minimum possible bag size)
        # 'high' starts at the maximum number in nums (largest bad size to consider)
        low, high = 1, max(nums) # min and max possible bags 

        # Perform binary search to find the minimum bag size
        while low < high:
            # Calculate the mid-point of the current range
            mid = (low + high) // 2

            # Calculate the total number of operations needed
            # to reduce each bag's size to at most 'mid'
            # (n - 1) // mid gives the number of splits needed for the bag 'n'.
            # Sum these operations for all bags
            if sum((n - 1) // mid for n in nums) <= maxOps: 
                # If the total operations are within the allowed limit(maxOps),
                # it means 'mid' is a feasible maximum bag size.
                # Narrow the search range by setting 'high' to 'mid'
                high = mid 
            else:
                # If  the total operations exceed maxOps, 
                # increase the minimum bag size by setting 'low' to 'mid +1'
                low = mid + 1 
        
        # After binary search, 'low' and 'high' converge to the minimum possible size
        return high
        
