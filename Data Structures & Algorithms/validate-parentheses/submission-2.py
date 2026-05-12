class Solution:
    def isValid(self, s: str) -> bool:
        matchingDict = {"{" : "}", "(" : ")", "[": "]"}
        stack = []
        for c in s:
            if c in matchingDict.keys():
                stack.append(c)
            elif c in matchingDict.values():
                if len(stack) == 0:
                    return False
                else:
                    if matchingDict[stack[-1]] != c:
                        return False
                    else:
                        stack.pop()
        return len(stack) == 0
            
        

