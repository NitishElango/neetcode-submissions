class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l,r = 0, 0
        seen = set()
        length = -1
        while r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                length = max(length, r - l + 1)
                r+=1
            else:
                l = l + 1
                r = l
                seen.clear()
            print(s[r: r+ length],length)
        return 0 if length == -1 else length