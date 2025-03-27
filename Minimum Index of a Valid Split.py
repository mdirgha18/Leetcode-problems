class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        lcount = 0 # Count of the dominant element in the left subarray

        # Find the most frequent element(domninant) and its count(recount)
        dominant, rcount = max(Counter(nums).items(), key = lambda x: x[1])

        # Iterate through the array, adjusting left and right counts
        for i, x in enumerate(nums):
            lcount += x == dominant # Increase the left count if element matches the dominant
            rcount -= x == dominant # Decrease the right count if element matches the dominant


            # Check if the dominant count is more than half in both left and right subarrays 
            if lcount > (i + 1) // 2 and rcount > (len(nums) - (i + 1)) // 2:
                return i # Return the index as soon as the conditions are met
        return -1        # Return -1 if no valid index is found
