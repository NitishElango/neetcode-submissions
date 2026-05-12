class Solution:
    def isPalindrome(self, s: str) -> bool:
        r = len(s) - 1
        l = 0

        s = s.lower()
        while(l < r):
            if(s[l].isalnum() == False):
                l+=1
                continue
            if(s[r].isalnum() == False):
                r-=1
                continue
            elif(s[l] == s[r]):
                l+=1
                r-=1
            else:
                return False
            
        return True