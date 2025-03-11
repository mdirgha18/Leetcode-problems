class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        count = 0 # Stores the total count of valid substrings 
        left = 0 # left pointer for the sliding window 
        char_count = {'a': 0, 'b':0, 'c': 0} # Dicitionary to track the occurences of 'a','b','c'


        # Iterate over the string with the right pointer
        for right in range(len(s)):
            char_count[s[right]] += 1 # Increase the count of the current character

            # Check if the window contains 
            while char_count['a'] > 0 and char_count['b'] > 0 and char_count['c'] > 0:
                count += len(s) - right # All substrings from current 'right' to end are valid 
                char_count[s[left]] -= 1 # Shrink the window from the left
                left += 1 # Move the pointer forward
        return count # Return the total number of valid substrings 
