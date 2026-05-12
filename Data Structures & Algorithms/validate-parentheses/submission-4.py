class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        trans = {"]" : "[", ")" :"(", "}":"{"}
        for c in s:
            if c in trans.values():
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack[-1] == trans[c]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0