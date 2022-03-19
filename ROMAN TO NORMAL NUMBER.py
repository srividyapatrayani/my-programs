class Solution:
    def romanToInt(self, s: str) -> int:
        d={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        before=0
        present=0
        total=0
        for i in range(len(s)):
            present=d[s[i]]
            if present>before:
                total=total+present-2*before
            else:
                total+=present
            before=present
        return total




        
