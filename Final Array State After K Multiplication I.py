
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        # Step 1: Create a list of tuples where each is (value, index) from the nums list 
        # This will help us track the original index of the numbers while using the heap
        pq = [(value, index) for index, value in enumerate(nums)]

        # Step 2: Convert the list of tuples into a heap (min-heap by default)
        heapq.heapify(pq)

        # Step 3: Perform 'k' iterations, wherein each iteration we update the value
        # at the root of the heap (smallest value) by multiplying it with 'multiplier'
        while k > 0:
            # Pop the smallest element from the heap (this returns a tuple: (value, index))
            value, index = heapq.heappop(pq)

            # Update the value in the original list 'nums' by multiplyinh it with 'multiplier'
            nums[index] = value * multiplier

            # Push the updated value back into the heap with the same index
            heapq.heappush(pq, (nums[index], index))

            # Decrease k after each operation
            k -= 1

        # Step 4: Return the updated list after performing 'k' operations
        return nums
