class Solution(object):
    def maximumTripletValue(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # Initialize variable to store the maximum triplet value 
        maxTriplet = 0 
        # Iterate over the first element (i)
        for i in range(len(nums)):
            # Iterate over the third element (k) from the end towards i + 1
            for k in range(len(nums) - 1, i, -1):
                j = i + 1 # Set j to be the middle element between j and k 

                # Iterate over j while it is strictly between i and k 
                while j < k:
                    # Calculate the triplet value and update maxTriplet if it is greater
                    maxTriplet = max(maxTriplet, (nums[i] - nums[j]) * nums[k])
                    j += 1 # Move the next middle element 
        
        # Ensure the result is non-negative (as negative values are not meaningful)
        return max(0, maxTriplet)
        
