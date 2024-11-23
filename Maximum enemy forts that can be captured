class Solution:
    def captureForts(self, forts: List[int]) -> int:
        if 1 not in forts or -1 not in forts: 
            return 0 
            
        out1 = [] #movement forward
        flag = False
        count1 = 0
        #Forward transversal
        for i in range(len(forts)):
            if forts[i] == 1: 
                flag = True
                count1 = 0 
            elif forts[i] == -1:
                flag = False 
                out1.append(count1)
                count1 = 0 
            elif flag and forts[i] == 0:
                count1 += 1

        fla = False
        out2 = []
        count2 = 0 

        #Backward reversal    
        for i in range(len(forts)-1, -1, -1): #Movement forward
            if forts[i] == 1:
                fla = True 
                count2 = 0
            elif forts[i] == -1:
                fla = False
                out2.append(count2)
                count2 = 0
            elif fla and forts[i] == 0:
                count2 += 1

        out1 += out2
        return max(out1)
        
