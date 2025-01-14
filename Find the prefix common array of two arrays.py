class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        # Get the length of the input arrays A and B
        n = len(A)
        
        # Initialize the set to keep track of elements we have seen so far
        seen = set()

        # Variable to keep track of the count of the common elements seen in the prefixes of A and B 
        C = [0] * n 

        # Iterate through each index of the arrays
        commonCount = 0
        for i in range(n):
            # Check if the current element of A is already in the 'seen' set
            if A[i] in seen:
                # If it is, increment the count of the common elements
                commonCount += 1
            else:
                # Otherwise, add it to the 'seen' set
                seen.add(A[i])
            
            # Check if the current element of B is already in the 'seen' set
            if B[i] in seen:
                # If it is, increment the count of common elements
                commonCount += 1
            else:
                # Otherwise, add it to the 'seen' set
                seen.add(B[i])
            
            # Update the current index of C with the current count of common elements
            C[i] = commonCount
        
        # Return the resulting array C
        return C
        
