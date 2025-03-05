class Solution:
    def coloredCells(self, n: int) -> int:
        # Formula to calculate the number of colored cells in a grid 
        # This formula is derived from the pattern of the colored cells in an expanding grid
        return 2 * n * n - 2 * n + 1
        
