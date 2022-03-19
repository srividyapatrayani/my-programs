class Solution:
    def isPalindrome(self, n:int) -> bool:
        k=n
        temp=0
        while(n!=0 and  n>=0):
            s=n%10
            temp=temp*10+s#1 #12 #121
            n=n//10
        if k==temp:
            return(True)
        else:
            return(False)



        
