class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        maxi = float('-inf') # Stores the maximum value of nums[i] encountered so farr
        diff = 0 # Stores the maximum (nums[i] - nums[j]) difference
        res = 0 # Stores the final maximum triplet value 

        # Iterate over the list
        for i in range(len(nums)):
            # Update the maximum value encountered so far
            maxi = max(maxi, nums[i])

            # Check if we have a valid triplet (at least 3 elements processed)
            if i >= 2: 
                res = max(res, diff * nums[i]) # Calculate and update the maximum triplet value
            
            # Check if we have at least two elements to calculate (nums[i] - nums[j])
            if i >= 1: 
                diff = max(diff, maxi - nums[i]) # Update the max difference (nums[i] - nums[j])

        return res # Return the maximum triplet value

        
