class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stk = []
        res = [0] * len(temperatures)
        for i in range(len(temperatures)):
            if not stk:
                stk.append((temperatures[i],i))
            else:
                print(stk)
                while stk and temperatures[i] > stk[-1][0]:
                    ind = stk.pop()[1]
                    dif = i - ind
                    res[ind] = dif
                stk.append((temperatures[i], i))
        return res

                    

