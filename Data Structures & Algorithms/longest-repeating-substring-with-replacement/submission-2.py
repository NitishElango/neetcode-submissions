class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        f = {}
        l,r =0,0
        maxc = 0
        longest = 0
        while r < len(s):
            if s[r] not in f:
                f[s[r]] = 1
            else:
                f[s[r]]+=1
            maxc = max(f.values())
            length = (r-l) + 1
            if length - maxc <= k:
                longest = max(longest, length)
            else:
                f[s[l]]-=1 
                l+=1
            r+=1
        return longest