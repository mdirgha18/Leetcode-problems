class Solution:
    def maximumLength(self, s: str) -> int:
        # Get the length of  the string 
        n = len(s)
        # Initialize the search range for the maximum length 
        l, r = 1, n

        # Check if the minimum length of 1 is valid using  helper function
        if not self.helper(s, n, l):
            return -1 # If it is not valid, return -1 as no valid length exists



        # Perform binary search to find the maximum valid length 
        while l + 1 < r:
            # Calculate the middle value of the current range
            mid = (l + r) // 2
            # If 'mid' is a valid, length, move the lower bound up
            if self.helper(s, n, mid):
                l = mid 
            else: 
                # Otherwise, move the upper bound down
                r = mid
        
        # The maximum valid length is store in 'l'
        return l

    def helper(self, s:str, n: int, x: int) -> bool:
        # Initialize a frequency counter for the characters (a-z)
        cnt = [0] * 26 
        # pointer to track the start of the substring
        p = 0 

        # Iterate through the string
        for i in range(n):
            # Move the pointer 'p' until 's[p]' matches 's[i]'
            while s[p] != s[i]:
                p += 1
            # Check if the substring length from 'p' to 'i' is at least 'x'
            if i - p + 1 >=x:
                # Increment the count for the current character
                cnt[ord(s[i]) - ord('a')] += 1
            # If any character count exceeds 2, return True (valid)
            if cnt[ord(s[i]) - ord('a')] > 2:
                return True
        
        # If no valid substing was found, return False
        return False
        
