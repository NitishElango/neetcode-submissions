class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) - 1
        s = s.lower()
        while l < r:
            if s[l].isalnum() and s[r].isalnum():
                if s[l] != s[r]:
                    return False
                else:
                    l+=1
                    r-=1
            elif s[l].isalnum() == False:
                l+=1
            elif s[r].isalnum() == False:
                r-=1
        return True