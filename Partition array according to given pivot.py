class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """

        n = len(nums) # Get the length of the input list 
        leftArr=[] # Stores elements smaller than the pivot 
        rightArr=[] # Stores elements greater than the pivot
        pivCnt = 0 # Count occurences of the pivot 

        # Traverse the array to count pivot elements and segregate elements
        for i in range(0,n): 
            if nums[i] == pivot: # Count occurences of the pivot 
                pivCnt+=1
            elif nums[i]>pivot: # If the element is greater than pivot, add to the rightArr
                rightArr.append(nums[i])
            else: # If the element is smaller than pivot, add to the leftArr
                leftArr.append(nums[i])

            
        # Construct the final array: left elements + pivot elements + right elements
        return leftArr+[pivot]*pivCnt+rightArr

        
