class Solution:
    def romanToInt(self, s: str) -> int:
        total = 0
        rtoi = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000,
        }
        i = 0
        while i in range(len(s)):
            if i == len(s) - 1:
                total += rtoi[s[i]]
                i+=1
            else:
                curr, nex = rtoi[s[i]], rtoi[s[i+1]]
                if nex > curr:
                    total += nex - curr
                    i+=2
                else:
                    total += curr
                    i+=1
        return total