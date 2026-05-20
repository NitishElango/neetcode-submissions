class Solution:
    def longestPalindrome(self, s: str) -> str:
        lp = ""
        for i in range(len(s)):
            l,r = i, i
            while l >= 0 and r < len(s) and s[r] == s[l]:
                    if r - l + 1 > len(lp):
                        lp = s[l:r+1]
                    l-=1
                    r+=1
        for i in range(1,len(s)):
            l,r = i-1, i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                    if r - l + 1 > len(lp):
                        lp = s[l:r+1]
                    l-=1
                    r+=1
        return lp
        
                    
            