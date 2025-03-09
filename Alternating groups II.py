class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        # Extend the colors list to handle the circular cases 
        colors.extend(colors[:(k-1)])
        count = 0 # Counter for valid alternating groups
        left = 0 # Left pointer for tracking the start of a valid group 


        # Iterate through the colors list using a sliding window approach
        for right in range(len(colors)):
            # Reset left pointer if two consecutive colors are same 
            if right > 0 and colors[right] == colors[right - 1]:
                left = right


            # If window size reaches k, it's a valid alternating group 
            if right - left + 1 >= k:
                count += 1

                
        # Return the total count of alternating groups of size k 
        return count

        
