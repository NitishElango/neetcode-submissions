class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        sol = [0] * len(temperatures)
        stk = []
        for i in range(len(temperatures)):
            temp = temperatures[i]
            if not stk:
                stk.append([temp,i])
            else:
                if stk[-1][0] >= temp:
                    stk.append([temp,i])
                else:
                    while stk and stk[-1][0] < temp:
                        val, ind = stk.pop()
                        sol[ind] = i - ind
                    stk.append([temp,i])
            print(stk)
        return sol
