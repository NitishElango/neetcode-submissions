class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        for c in tokens:
            if c.lstrip('-').isdigit():
                stk.append(c)
                continue
            if len(stk) >=2:
                num1, num2 = stk.pop(), stk.pop()
            if c == '+':
                stk.append(int(num2) + int(num1))
            if c == "-":
                stk.append(int(num2) - int(num1))
            if c == "*":
                stk.append(int(num2) * int(num1))
            if c == "/":
                stk.append(int(int(num2) / int(num1)))
            print(stk)
        return int(stk[-1])
