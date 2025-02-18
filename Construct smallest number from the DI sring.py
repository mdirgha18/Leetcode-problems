class Solution(object):
    def smallestNumber(self, pattern):
        """
        :type pattern: str
        :rtype: str
        """
        # Given a pattern of 'I' (increasing) and 'D'(decreasing)
        # this function generates the lexicographically smallest number
        # that follows the patter using digits 1-9 without repetition
        ans, temp = ["1"], [] # Initialize result list with the first digit
         # Temporary stack to store decreasing sequence
         # Iterate through each pattern characters
        for i, ch in enumerate(pattern):
            if ch == 'I':
                # If 'I' (increasing), reverse the temp stack and append the next number
                ans += temp[::-1] + [str(i+2)]
                temp = [] # Reset temp for next sequence
            else:
                # If 'D' (decreasing), store the last number in temp and add the next number
                temp.append(ans.pop())
                ans.append(str(i+2))
        
        # Concatenate the result list with any remaining reversed temp values and return the final number
        return "".join(ans + temp[::-1])
        
