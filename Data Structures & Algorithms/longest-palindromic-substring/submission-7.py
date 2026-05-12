class Solution:
    def longestPalindrome(self, s: str) -> str:
        max_l, max_s = -1, ""
        for i in range(len(s)):
            l = r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length = r - l + 1
                if length > max_l:
                    max_l = length
                    max_s = s[l:r+1]
                l-=1
                r+=1
        print(max_s)
        print(max_l)
        for i in range(len(s)-1):
            l,r = i, i + 1
            print(i,l,r,s[l],s[r])
            while l >= 0 and r < len(s) and s[r] == s[l]:
                length = r - l + 1
                if length > max_l:
                    max_l = length
                    max_s = s[l:r+1]
                l-=1
                r+=1
        return max_s
            