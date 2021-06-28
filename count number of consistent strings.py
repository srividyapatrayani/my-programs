class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        for w in words:
            tp = True
            for el in w:
                if el not in allowed:
                    tp = False
                    break
            if tp:
                count += 1
        return count
        
