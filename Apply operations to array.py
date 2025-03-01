class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        n = len(nums) # Get the length of the list 

        # Apply operations 
        # If two consecutive elements are equal, then double the first one and set the second one to 0
        for i in range(n - 1):
            if nums[i] == nums[i + 1]: # Check if adjacent elements are same
                nums[i] *= 2 # Double the first element 
                nums[i + 1] = 0 # Set the second element to zero 

        # Shift zeros to the end (in-place)
        non_zero_idx = 0 # Pointer to track the position of next non-zero element

        # MOve all the non-zero elements to the front 
        for i in range(n):
            if nums[i] != 0: # If the current element is non-zero
                nums[non_zero_idx] = nums[i] # Move it to the 'non-zero-idx' position
                non_zero_idx += 1 # Increment the non-zero index

        # Fill the remaining positions with zeros 
        for i in range(non_zero_idx, n): 
            nums[i] = 0 # Set the remaining elements to zero 

        return nums # Return the modified list
        
