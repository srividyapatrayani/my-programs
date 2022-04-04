class Solution:
    def isPalindrome(self, s: str) -> bool:
        S=s.lower()
        l=[]
        for i in S:
            if i.isalnum():
                l.append(i)
        print(l)
        m=0
        n=len(l)-1
        while(m<=n):
            if l[m]!=l[n]:
                return False

            m+=1
            n-=1
                #pprint(m,n)
        return True
        
        '''if(l[0:]==l[::1]):
            return True
        else:
            return False'''
