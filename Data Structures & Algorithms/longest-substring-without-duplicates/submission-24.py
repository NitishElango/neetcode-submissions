class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = r = 0
        seen = set()
        while r < len(s):
            #new char - expanding window
            if s[r] not in seen:
                seen.add(s[r])
                r+=1
                longest = max(longest, (r-l))
            elif s[r] in seen:
                #shrinking window
                while s[l] != s[r]:
                    seen.remove(s[l])
                    l+=1
                #skip the dup
                l+=1
                r+=1
        return longest
