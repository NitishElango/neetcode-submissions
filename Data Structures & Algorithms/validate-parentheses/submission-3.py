class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        o = {"]":"[", ")":"(", "}":"{"}
        for b in s:
            if b in o.values():
                stack.append(b)
            else:
                if len(stack) == 0:
                    return False
                elif stack[-1] == o[b]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0