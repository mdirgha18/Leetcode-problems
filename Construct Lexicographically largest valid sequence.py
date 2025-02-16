class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        # Initialize the result array with zerod, lenght is 2*n - 1
        result = [0] * (2 * n - 1)
        # Boolean list to traack which numbers have been used
        used = [False] * (n+1)

        # Start backtracking to fill the sequence
        self.backtrack(result,used,n,0)
        return result

    def backtrack(self, result: List[int], used: List[bool], n: int, index: int) -> bool:
        
        # Move the next available index if the current position is already filled
        while index < len(result) and result[index] != 0:
            index +=1

        # If we have filled the entire sequence,  return true (successful case)
        if index == len(result):
            return True

        # Try placing numbers from n down to 1 (to maintain lexicographical order)
        for i in range(n, 0, -1):

            if used[i]: # Skip if the number is already used
                continue

            if i == 1:
                # if i is 1, it appears only once, do place it at index
                result[index] = 1
                used[i] = True
                # Recursively try to fill the remaining sequence
                if self.backtrack(result, used, n, index + 1):
                    return True
                # Backtrack if no valid sequence is found
                result[index] = 0
                used[i] = False
            elif index + i < len(result) and result[index + i] == 0:
                # If placing i at index and index + i isvalid (both positions are empty)
                result[index] = i 
                result[index +i] = i
                used[i] = True
                # Recursively try to complete the sequence
                if self.backtrack(result, used, n, index + 1):
                    return True
                # Backtrack if it does not lead to the solution
                result[index] = 0
                result[index + i] = 0
                used[i] = False
        # If no valid sequence is found, return false
        return False 

        
