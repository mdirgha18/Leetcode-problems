class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # If the length of the string is less than k, it's impossible to construct k palindromes
        if len(s) < k:
            return False 
        
        # Importing counter from collections to count the frequency of the characters in the string
        from collections import Counter
        freq = Counter(s) # Get a dictionary with the frequency of each character in the string

        # Calculate the number of characters with an odd frequency
        # A character with an odd frequency can only appear in one palindrome's center
        odds = sum(1 for count in freq.values() if count % 2 != 0)

        # Check if the number of odd-frequency characters is less than or equal to k 
        # This ensures that we can distribute the odd characters among the k- palindromes

        return odds <= k  
