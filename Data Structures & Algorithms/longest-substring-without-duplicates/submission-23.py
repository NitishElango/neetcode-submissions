class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        maxc = 0
        seen = set()
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
                diff = r - l
                maxc = max(diff, maxc)
            elif s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l+=1
                if s[l] == s[r]:
                    l+=1
                    r+=1
        return maxc
