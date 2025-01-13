class Solution:
    def minimumLength(self, s: str) -> int:
        # Initialize an array to strore the frequency of each character (a-z)
        arr = [0] * 26


        # Count the frequency of each character in the strong
        # Continuing the char
        for ch in s:
            # ord(ch) - ord('a') gives the index for the character 'ch' 
            arr[ord(ch) - ord('a')] += 1

        # Applying the rules for reducing the frequency of characters
        # Rule: If a character appears 3 or more times, reduce it by 2 occurences
        for i in range(26):
            while arr[i] >= 3:
                arr[i] -= 2 # Reduce the count by 2 for this character

        # Counting the length of the final string
        # Calculate the length of the result string after applying the rules
        # Sum up the remaining counts of characters (the final string length)
        length = sum(arr)

        # Retun the calculated length
        return length

        
