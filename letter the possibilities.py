class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        # Given a string 'tiles', this function calculates the number of possible non-empty sequences
        # that can be formed using the letters in 'tiles'

        # Count occurences of each tile using a counter (dictionary-like structure)
        count = collections.Counter(tiles)
        def dfs(count: dict[int, int]) -> int:

            # Performs depth-first search (DFS) to  explore all possible sequences 
            # This recursively reduces the count of tiles, forming different combinations
            possibleSequences = 0 # Counter for valid sequences

            # Iterate over eahc unique tile and its remaining count
            for k, v in count.items(): 
                if v == 0: # Skip tiles that have been fully used
                    continue
                
                # Use one occurence of the current tile
                count[k] -= 1

                # Count this sequence and continue searching for more possibilities
                possibleSequences += 1 + dfs(count)

                # Backtrack: Restore the count of the tile for the next iteration
                count[k] += 1
            return possibleSequences

        # Start the DFS traversal
        return dfs(count)
        
