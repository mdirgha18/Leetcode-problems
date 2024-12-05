class Solution:
    def canChange(self, s: str, t: str) -> bool:
        # Length of the strings  
        n=len(s)

        # Append a '0' to both strings to handle edge cases (end of the string)
        s+='0'
        t+='0'

        # Initialise pointers for both strings 
        i, j=0, 0

        # Loop untill we process all characters in both strings 
        while i<n or j<n:
            # Skip all '_' characters in strings s
            while i<n and s[i]=='_': i+=1
            # Skip all '_' characters in strings t
            while j<n and t[j]=='_': j+=1
            
            # Compare the characters at the current pointers
            c=s[i]
            if c!=t[j]: return False # If the characters are different, transformation is not possible

            # Check if an 'L' character violates the movement rule
            # 'L' can only move to the left, so its index in t(j) must not be greater than its index in s(i)
            if c=='L' and i<j: return False
            # 'R' can only move to the right, so its index in t(j) must not be less than its index in s(i)
            if c=='R' and i>j: return False

            # Move both pointers forward
            i+=1
            j+=1

        # if all checks pass, transformation is possible
        return True

        
