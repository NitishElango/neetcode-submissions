class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for t in tokens:
            if len(t) >= 2:
                stk.append(int(t))
            elif t.isdigit():
                stk.append(int(t))
            else:
                print(stk)
                num2 = stk.pop()
                num1 = stk.pop()
                if t == "+":
                    stk.append(num1 + num2)
                elif t == "-":
                    stk.append(num1-num2)
                elif t == "*":
                    stk.append(num1*num2)
                else:
                    stk.append(int(num1/num2))
        return stk[-1]
