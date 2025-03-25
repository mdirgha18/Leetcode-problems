class Solution(object):
    def checkValidCuts(self, n, rectangles):
        """
        :type n: int
        :type rectangles: List[List[int]]
        :rtype: bool
        """
        # Check if a valid cut exists along either the x-aixs or y-axis 
        # Calls isValidCut twice: once sorting by x1 (index 0) and once sorting by y1 
        return self.isValidCut(rectangles, 0, 0, 2) or self.isValidCut(rectangles, 1, 1, 3)
    
    def isValidCut(self, rectangles, sort_index, start, end):

        # Sort rectangles based on the chosen coordinate (x1 or y1)
        rectangles.sort(key=lambda x: x[sort_index])

        # Initialize the first interval's start and end values 
        current_start = rectangles[0][start]
        current_end = rectangles[0][end]
        intervals = 0 # Counter for the distinct groups 


        # Iterate through the sorted rectangles to find the seperate groups 
        for rect in rectangles:
            if rect[start] < current_end: # If overlapping or touching, extend  the current interval 
                current_end = max(rect[end], current_end)

            else: # if not overlapping, a new interval starts 
                intervals += 1
                current_start = rect[start]
                current_end = rect[end]

        # Count the last intervals 
        intervals += 1

        # If there are more than two distinct groups, return True-
        return intervals > 2 

        
