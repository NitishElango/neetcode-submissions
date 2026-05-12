class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        freq = dict()
        l,r = 0 , 0
        maxl = 0
        while r < len(s):
            if s[r] in freq:
                freq[s[r]] +=1
            else:
                freq[s[r]] = 1
            r+=1

            while (r - l) - max(freq.values()) > k:
                freq[s[l]] -= 1
                l+=1
            maxl = max(maxl, r - l)
        return maxl