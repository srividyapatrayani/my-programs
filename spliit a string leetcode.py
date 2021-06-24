class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        answer = 0
        for character in s:
            if character == 'R':
                balance += 1
            else:
                balance -= 1
            if balance == 0:
                answer += 1
        return answer
        
