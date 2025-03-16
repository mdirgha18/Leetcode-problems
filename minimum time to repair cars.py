class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        left = 1 # Minimum possible repair time 
        right = min(ranks) * cars * cars # Worst-case maximum time 


        # Function to check if all the cars can be repaired at all the times 
        def can_repair_all(time): 
            total_cars_repaired = 0 
            for rank in ranks:
                # Each mechanic repairs sqrt(time/rank) cars in 'time' minutes
                cars_repaired = int((time / rank) ** 0.5)
                total_cars_repaired += cars_repaired
                if total_cars_repaired >= cars: # If we repair enough cars, return True
                    return True
            return False # Not enough cars repaired 

        # Perform binary search to find the minimum time 
        while left < right: 
            mid = (left + right) // 2 # Midpoint of current search space 
            if can_repair_all(mid): # If possible, try for a smaller time 
                right = mid 
            else: # If not possible, increase time 
                left = mid + 1

        return left # The minimum time required to repair all the cars 
        
