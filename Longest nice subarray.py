class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        # Get the length of the array
        # Answer keeps the track of the maximum subarray length
        # B stores the bitwise OR of the current subarray 
        # l is the left pointer of the sliding window
        n, ans, B, l=len(nums), 0, 0, 0

        # Iterate through the array with the right pointer (r)
        for r, x in enumerate(nums):
            # If adding x causes a conflict (common bits exist), move the left pointer
            while l<r and (B & x)!=0:
                # Remove nums[l] from the bitwise OR by using XOR
                B^=nums[l]
                # Move the left pointer forward 
                l+=1
            # Add the current number x to the bitwise OR of the subarray 
            B|=x
            # Update the maximum subarray length found so far
            ans = max(ans, r-l+1)
        
        # Return the maximum length of the "nice" subarray
        return ans

        
