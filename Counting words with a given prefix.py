class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        # Initialize the counter to track  the number of words matching the prefix 
        c = 0 

        # Get the length of the prefix
        n = len(pref)

        # Iterate through each word in the list
        for word in words:
            # Check if the word is as long as the prefix
            # and if the first 'n' characters of the word match the prefix 
            if len(word) >= n and word[:n] == pref:
                # If the word starts with the prefix, increment the counter
                c += 1

        # Return the total count of the words that match the prefix
        return c


        
