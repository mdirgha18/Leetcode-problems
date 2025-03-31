class Solution(object):
    def putMarbles(self, weights, k):
        """
        :type weights: List[int]
        :type k: int
        :rtype: int
        """
        n = len(weights) - 1 # Number of adjacent pairs 

        # Compute the sum of adjacent pairs 
        weights = [weights[i] + weights[i + 1] for i in range(n)]

        # Sort the pair sums in ascending order
        weights.sort()

        res = 0 # Variable to store the result

        # Compute the difference between the largest (k - 1) and smallest (k - 1) values
        for i in range(k - 1):
            # Difference between largest and smallest pairs 
            res += weights[-1 - i] - weights[i]

            # Return the final computed values 
        return res
        
