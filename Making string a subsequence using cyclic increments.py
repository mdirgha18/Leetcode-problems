class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        cur_idx = 0 #Initialize the current index for the iterating through str1 

        for i in range(len(str2)): # Iterate through characters in str2
            psbl = False #Initialize a flag to track if a valid character match is found 
            for j in range(cur_idx, len(str1)): # Iterate through remaining characters in str1
            # Check if the characters match directly, are consecutive in ASCII or are 'a' and 'z'
                if str2[i] == str1[j] or ord(str2[i]) - ord(str1[j]) == 1 or (str2[i] == "a" and str1[j] == "z"):
                    psbl = True #Set the flag to indicate a valid match is found 
                    cur_idx = j + 1 # Update the current index in str1 for the next iteration
                    break #Exit the inner loop since a match is found 
                
            if not psbl: # If no valid match is found for a character in str2
                return False # Return False since str1 cannot form str2 as a subsequence
        return True #All characters in str2 have valid matches in str1, so no returning true 
                    
        
