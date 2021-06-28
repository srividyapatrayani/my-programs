class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        if {'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'}.issubset(set(sentence)):
            return True
        return False
