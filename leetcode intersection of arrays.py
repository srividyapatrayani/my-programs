class Solution:
    def NumberofElementsInIntersection(self,a, b, n, m):
        a=set(a)
        b=set(b)
        a=a.intersection(b)
        return len(a)
