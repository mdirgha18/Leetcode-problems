class Solution:
    def findChampion(self, n: int, edges: List[List[int]]) -> int:
        # Initialize a list to track if each team is undefeated (True means undefeated)
        isUndefeated = [True] * n 

        #Iterate over each match outcome in edges
        for winner, loser in edges:
            # Mark the loser of each match as defeated
            isUndefeated[loser] = False 

        # Initialize variables to store the potential champion and the count of undefeated teams
        champion = -1 
        championCount = 0

        # Iterate over all teams to check if they are undefeated
        for team in range(n):
            if isUndefeated[team]:

                # If the team is undefeated, set it as the champion and increment the count
                champion = team 
                championCount += 1
        # If there's exactly one undefeated team, return it as the champion
        if championCount == 1:
            return champion 
        
        # If there are zero or more than one undefeated teams, return 01 (no unique champion)
        return -1
        
