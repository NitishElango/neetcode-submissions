class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        sol = [0] * n
        sol[0] = 1
        sol[1] = 2
        for i in range(2, n):
            sol[i] = sol[i-1] + sol[i-2]
        print(sol)
        return sol[-1]

        
        