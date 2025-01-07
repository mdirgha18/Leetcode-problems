class Solution:
    # Method to find all the words in the list that are substrings of other words
    def stringMatching(self, words: List[str]) -> List[str]:
        # Get the number of words in the input list
        n = len(words)

        # Initialise an empty list to store the result
        ans = []

        # Loop through each word in the list (indexed by i)
        for i in range(n):
            # Compare the current word with every other word in the list 
            # Check if words are not the same (i!= j)
            # and if the word at index i is a substring of the word at index j
            for j in range(n):
                if i != j and words[j].find(words[i]) != -1:
                    # If the condition is satisfied, add the word at index i to the result list
                    ans.append(words[i])
                    # Break the inner loop once a match is found to avoid duplicate additions
                    break 
        # Return the final list of words that are substrings of the other words
        return ans
        
