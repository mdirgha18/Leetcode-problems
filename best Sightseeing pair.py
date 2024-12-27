class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        # Number of elements in values array
        n = len(values)

        # Initialize an array to store the maximum values of the suffix computations 
        # suffixMax[i] will store the maximum value of values[j] - j for j >= 1
        suffixMax = [0] * n
        # Compute the suffix max for the last element
        suffixMax[n-1] = values[n-1] - (n-1)

        #Populate the suffixMax array from right to left 
        for i in range(n-2, -1,-1):
            # At each index, take maximum of the next suffix value
            suffixMax[i] = max(suffixMax[i+1], values[i] - i)
            # or the current value adjusted by its index

        maxScore = float('-inf')

        # Iterate through the array (except the last element)
        for i in range(n-1):
            # calculate the sightseeing pair as values[i] + i + suffixMac[i+1]
            # Update the maximum score if the current score is higher
            maxScore = max(maxScore, values[i] + i + suffixMax[i + 1])

        # Return the maximum sightseeing score
        return maxScore

        
