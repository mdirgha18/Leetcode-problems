class Solution:
    def minOperations(self, nums: List[int]) -> int:
        # Get the length of the array
        # i0 stores of the index of the first zero round 
        # op keeps the track of number of operations 
        # Append an extra zero to avoid the index out-of-bounds errors 
        # Infinite loop to keep finding zeros and flipping bits  
        n, i0, op = len(nums), -1, 0
        nums.append(0)
        while True:
            # Find the next occurence of zero starting from (i0 + 1)
            i0 = nums.index(0, i0+1)

            # If the found near zero is near the end, we cannot perform operations 
            if i0 >= n-2:
                break

            # Flip the bits of the next two elements 
            nums[i0+1] ^=1
            nums[i0+2] ^=1

            # Increment operation count 
            op+=1

        # If all the zeros were removed, return the operation count; otherwise, return -1
        return op if i0>=n else -1
        
