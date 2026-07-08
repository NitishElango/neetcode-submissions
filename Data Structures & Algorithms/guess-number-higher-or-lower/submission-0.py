# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l,r = 0 , n
        while l <= r:
            num = (l+r)//2
            if guess(num) == 0:
                return num
            elif guess(num) == 1:
                l = num + 1
            else:
                r = num - 1
