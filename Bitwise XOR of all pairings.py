class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        # Initialize variables to store the XOR of all elements in nums1 and nums2
        xor1 = 0 
        xor2 = 0

        # Compute the XOR of all elements in nums1
        for num in nums1:
            xor1^= num # XOR operation to accumulate the result

        # Compute the XOR of all elements in nums2
        for num in nums2:
            xor2^= num # XOR operation to accumulate the result

        # Initialize the result variable
        result = 0 

        # If the length of nums2 is odd, include the XOR of all elements in nums1
        # This is because each element in nums1 will appear in the XOR result
        # an odd number of times when paired will all elements in nums2
        if len(nums2) % 2 == 1:
            result ^= xor1 # Add the XOR of nums1 to the result

        # If the length of nums1 is odd, include the XOR of all elements in the nums2
        # This is because each element in nums2 will appear in the XOR result
        # an odd number of times when paired with all elements in nums1
        if len(nums1) % 2 == 1:
            result ^= xor2 # Add the XOR of nums2 to the result

        
        # Return the final XOR result
        return result
        
