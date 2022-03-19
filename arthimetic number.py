class Solution:
    def inSequence(self, A, B, C):
        if A==B:
            return 1
        elif C==0:
            return 0
        elif((B-A)%C==0 and (B-A)/C>0):
            return 1
        
            
        else:
            return 0
        # code here
