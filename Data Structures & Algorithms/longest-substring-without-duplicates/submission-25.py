class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        seen = set()
        max_s = 0
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
                max_s = max(max_s, (r-l))
            elif s[r] in seen:
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l+=1
                l+=1
                r+=1
        return max_s
