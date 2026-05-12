class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk = []
        ops = set(["+","-","*","/"])
        for n in tokens:
            res = 0
            if n not in ops:
                stk.append(int(n))
            else:
                pop1, pop2 = int(stk.pop()), int(stk.pop())
                if n == "+":
                    res = pop1 + pop2
                elif n == "-":
                    res = pop2 - pop1
                elif n == "*":
                    res = pop1 * pop2
                else:
                    res = pop2 // pop1
                    if res < 0:
                        res = math.ceil(pop2/pop1)
                stk.append(res)
        return stk[-1]