class Solution:
    def interpret(self, command: str) -> str:
        results = ""
        index = 0
        
        while index < len(command) :
            if command[index:index +4] == "(al)" :
                results += "al"
                index += 4
            elif command[index:index + 2] == "()" :
                results += "o"
                index += 2
            else :
                results += "G"
                index += 1
        return results
