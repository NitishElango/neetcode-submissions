class Solution:
    def isValid(self, s: str) -> bool:
        # initializing the variables
        stack = []
        openDict = {0: "(", 1:"{",2:"["}
        closeDict = {")": 0, "}": 1, "]": 2}

        # iterating
        for i in range(len(s)):
            if s[i] in closeDict:
                if len(stack) == 0:
                    return False
                else:
                    if openDict[closeDict[s[i]]] != stack[-1]:
                        return False
                    else:
                        stack.pop()
            elif s[i] in openDict.values():
                stack.append(s[i])
        
        #final check
        return len(stack) == 0