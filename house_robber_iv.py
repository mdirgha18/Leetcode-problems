class Solution(object):
    def canRob(self,nums,mid,k):
        count = 0 # Number of houses we can rob 
        n = len(nums) # Total number of houses
        i = 0 # Pointer to iterate through houses
        while i < n:
            if nums[i] <=mid: # If the house value is <= mid, we can rob it 
                count += 1 # Increment the count of the robbed houses
                i += 1 # Skip the next house to avoid robbing the adjacent house
            i += 1 # Move to the adjacent next house
        return count >= k # Return true if we can rob at least k houses

    def minCapability(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        left, right = 1, max(nums) # Define search range from 1 to max house value
        ans = right # Store the minimum maximum houses
        while left <= right: 
            mid = (left + right) // 2 # Find the middle value as the potential answer
            if self.canRob(nums, mid, k): # Check if it is possible with this mid value
                ans = mid # Update answer if it is valid
                right = mid - 1 # Try to minimize the max house 
            else:
                left = mid + 1 # Increase mid because it is too small
        return ans # Return the minimum possible max value
        
