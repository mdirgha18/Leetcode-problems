class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        m, n = len(str1), len(str2)

        # Step 1: Compute LCS table using dyynamic programming
        # dp[i][j] represents the length of the longest common subsequence (LCS)
        # for substrings str1[0:1] and str2[0:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        
        # Fill the LCS table 
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if str1[i - 1] == str2[j - 1]: # Characters match, extend LCS 
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else: # Take the maximum LCS length from the previous subproblems 
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # Step 2: Build the shortest supersequence using the LCS table
        i, j = m, n # Start from the bottom right corner of the table
        result = [] # To store the supersequence characters 

        while i > 0 and j > 0:
            if str1[i - 1] == str2[j - 1]:  # If characters match, add to result
                result.append(str1[i - 1])
                i, j = i - 1, j - 1 # Move diagonally in the table 
            elif dp[i - 1][j] > dp[i][j - 1]:  # Move in the direction of max LCS value
                result.append(str1[i - 1]) # Add the character in str1
                i -= 1 # Move up in the table 
            else:
                result.append(str2[j - 1]) # Add character from str2
                j -= 1 # Move left in the table 

        # Step 3: Add remaining characters from either string
        while i > 0:
            result.append(str1[i - 1])
            i -= 1
        while j > 0:
            result.append(str2[j - 1])
            j -= 1


        # Step 4: Reverse to get the correct order
        return "".join(result[::-1])  # Reverse to get correct order
