class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        n1, n2 = len(nums1), len(nums2) # Get length of both the lists 
        ans=[] # List to store the merged result
        i, j=0, 0 # Pointers for nums1 and nums2

        # Merge two lists while maintaining sorted order 
        while i<n1 or j<n2: 
            # If one list is exhausted, set a ID value for comparison
            id1=2000 if i == n1 else nums1[i][0] # If nums1 is exhausted, set id1 to 2000
            id2=2000 if j == n2 else nums2[j][0] # If nums2 is exhausted, set id2 to 2000
            if id1==id2: # If both the lists have the same ID 
                ans.append([id1, nums1[i][1] + nums2[j][1]]) # Sum their values and add to the result
                i+=1 # Move both the pointers forward
                j+=1
            elif id1<id2: # If the ID from nums1 is smaller, add it to the result
                ans.append(nums1[i])
                i+=1 
            else: # If the ID from nums2 is smaller, add it to the result
                ans.append(nums2[j])
                j+=1
        return ans # Return the merged list
        
