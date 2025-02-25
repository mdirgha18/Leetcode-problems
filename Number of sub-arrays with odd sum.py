class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        # Tracks whether the cumulative sum up to the current index is odd(1) or even(0)
        sum_is_odd = 0

        # A count array to store the number of times we have seen (cnt[0]) and odd(cnt[1]) sums
        cnt = [1,0] # cnt[0] = 1 handle cases where the first array itself is odd

        # Variable to store the final count of the subarrays with an odd sum
        ans = 0

        # iterate through the array 
        for x in arr:
            # Update sum_is_odd: XOR with (x & 1) to determine if the sum remains even or becomes old 
            sum_is_odd ^= (x & 1)

            # if sum_is_odd is 1 (odd sum), add count of even sums seen so far 
            # if sum_is_even is 0 (even sum), add count of odd sums seen so far

            ans+=cnt[1-sum_is_odd]

            # Increment the count of the current sum state (either even or odd)
            cnt[sum_is_odd]+=1
        
        # Return the result modulo 10^9+7 to prevent integer overflow
        return ans%(10**9+7)
        
