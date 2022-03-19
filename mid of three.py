class Solution:
    def middle(self,A,B,C):
        if (A-B)*(A-C) <0:
            return A
        elif(B-A)*(B-C) <0:
            return B
        else:
            return C
            
            
            
            #app2
            class Solution:
    def middle(self,A,B,C):
        c=min(A,B,C)
        d=max(A,B,C)
        a=c^d^A^B^C
        return a
