class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxC=max(candies)
        sol=[]
        for i in candies:
             if i+extraCandies>=maxC:
                sol.append(True)
             else:
                sol.append(False)
        return sol
        
