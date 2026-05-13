class Solution:
    def numDecodings(self, s: str) -> int:
        n = len(s)
        self.cache = dict()
        def dfs(ind):
            r,l =  0,0
            if ind in self.cache:
                return self.cache[ind]
            if ind == n:
                return 1
            else:
                if ind < n:
                    if s[ind] == "0":
                        return 0
                    l = dfs(ind + 1)
                if ind + 1 < n:
                    if s[ind] == "0":
                        return 0
                    else:
                        dig = s[ind] + s[ind+1]
                        if int(dig) >= 1 and int(dig) <= 26:
                            r = dfs(ind + 2)
            self.cache[ind] = r + l
            return r + l
        return dfs(0)