class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # Finds the maximum count between positive and negative numbers in a sorted array


        # Count of the negative numbers (index of first 0)
        neg_count = self.binary_search(nums,0)

        # Count of positive numbers (total elements - index of the first positive number)
        pos_count = len(nums) - self.binary_search(nums, 1)

        # Return the maximum of two counts
        return max(neg_count, pos_count)

    def binary_search(self, nums, target):

        # Custom binary search to find the first occurence of the target in the sorted array 
        # If 'Target' is 0, it finds the first non-negative index (i.e. count of the negative numbers )
        # If the target is '1', finds the first positive index 
        left, right = 0, len(nums) - 1
        result = len(nums) # Default result if the target was not found 

        while left <= right:    
            mid = (left + right) // 2   # Find the middle index 
            if nums[mid] < target:
                left = mid + 1
            else: 
                # If the mid value is greater than or equal, update the result and move right boundary leftward 
                result = mid
                right = mid - 1
        return result   # Return the first index where 'target' could be inserted 
