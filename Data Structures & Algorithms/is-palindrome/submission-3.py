class Solution:
    def isPalindrome(self, s: str) -> bool:
        rp = len(s) - 1
        lp = 0
        sl = s.lower()
        while lp <= rp:
            if sl[lp].isalnum() == False:
                lp = lp + 1
            elif sl[rp].isalnum() == False:
                rp = rp - 1
            elif sl[lp] != sl[rp]:
                return False
            else:
                rp = rp - 1
                lp = lp + 1
        return True